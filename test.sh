#!/bin/sh
# $1 = test_blackbox.py::test_order_ingest_data
# if test -z "$1 == 'load'"
# then
#     locust -f locust_files/my_locust_file.py --master --host=$2 &
#     locust -f locust_files/my_locust_file.py --slave --host=$2
#     exit
# fi

if test -z "$1"
then
    python -m pytest -s --disable-warnings
else
    # pytest-watch --runner "python -m pytest -s --disable-warnings tests/$1"
    python -m pytest -s --disable-warnings tests/$1
    # python -m ptw
fi
