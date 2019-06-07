#! /usr/bin/env python

from japronto import Application
import datetime
import itertools
import random
import threading

# must be less than 256
labrinth_size = 100

wait_time_us = 1200

# Make the code repeatable
random.seed(943857634)

lock = threading.Lock()
state = {'start_time': datetime.datetime.now()}


def get_labyrinth_paths():
    labyrinth = [i for i in range(1, labrinth_size)]

    random.shuffle(labyrinth)
    rabbit_location = labyrinth[-1]

    prev = 0
    list = []
    for i in labyrinth:
        list.append([prev, i])
        prev = i

    random.shuffle(list)

    return (rabbit_location, bytes(itertools.chain(*list)))


rabbit_location, paths = get_labyrinth_paths()


def start(request):
    """Handles the start route, returns the labyrinth"""
    lock.acquire()
    state['start_time'] = datetime.datetime.now()
    lock.release()
    return request.Response(body=paths)


def look(request):
    lock.acquire()
    start = state['start_time']
    lock.release()
    microseconds = ((datetime.datetime.now() - start)
                    / datetime.timedelta(microseconds=1))
    place = int(request.path.split('/')[2])
    if rabbit_location != place:
        text = 'no rabbit here'
    elif microseconds > wait_time_us:
        text = ('You made it through the labrinth but the rabbit already left.'
                ' It took %dμs' % microseconds)
    else:
        text = 'You found the white rabbit. It took %dμs' % microseconds

    return request.Response(text=text)


if __name__ == "__main__":
    app = Application()
    app.router.add_route('/start', start)
    app.router.add_route('/look/{place}', look, 'GET')
    app.run(debug=False)
