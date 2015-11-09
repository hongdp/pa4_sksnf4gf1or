### Group Name: group88

### Members:
  - Penghua Zhao (phzhao)
  - Dapeng Hong (hongdp)
  - Chengwei Dai (joedai)

### Link to homepage
  - [Link For Running Version](http://eecs485-09.eecs.umich.edu:5688/sksnf4gf1or/pa4/search)

### Details:
  - We use c++ library
  - We are using the same schema as PA3, Album Photo Contain
  - We use port 6288 for c++ indexserver

### Deploy:
  - `cd pa4/python/`
  - `virtualenv venv --distribute`
  - `source venv/bin/activate` (run for every new terminal window)
  - `pip install -r requirements.txt`
  - `gunicorn -b eecs485-09.eecs.umich.edu:5688 -b eecs485-09.eecs.umich.edu:5788 -w 4 -D app:app`
  - go to link above

### Reset Database:
  - Run sql/load_xml.sql in mysql

