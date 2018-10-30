# Rating Fetcher
- Easily Fetch your ratings across multiple competitive programming platforms
- Currently Supports
  - Codeforces
  - Hackerrank
  - Codechef

## Installation
**This tool works only with Python 3**
- To install the dependencies run `$ pip install -r requirements.txt`
- You need to have `geckodriver` installed in order to run this tool

## Usage
- For using 
```
$ python get_rating <hackerrank_handle> <codechef_handle> <codeforces_handle>
```
- However if you wish to get ratings from individual websites , you can use `-cc` for Codechef , `-cf` for codeforces , `-hr` for hackerrank followed by the username
```
$ python get_rating.py <-cc "Codechef handle"> | <-cf "codeforces handle"> | <-hr "Hackerrank Handle">
```
- examples:
```
$ python get_rating.py -cc pieliedie -hr abhiy13 -cf abhiroxx
// gets all ratings

$ python get_rating.py -cc pieliedie -hr abhiy13
// gets ratings only from codechef and hackerrank

python get_rating.py -cc pieliedie
//gets rating only from codechef
```

## For testing
- For testing run 
  - `python get_rating.py --test`

## Fetching mechanism for many other websites will be integrated soon.
