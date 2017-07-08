# GuessThatSong

GuessThatSong is a webapp which plays a randomly selected song and gives a 
multiple choice quiz on which song it is. Assumes music directory is local and
organized, and the path is configurable.

Example App at http://guessthatsong.herokuapp.com

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
flask
sqlalchemy
```

### Installing

```
clone git https://github.com/mattmurch/GuessThatSong.git
python setup.py install
```

* On site deployment, answer 'yes' when asked if you would like to update your database.
* Songs must be located in app/static/ directory
* This application assumes music is organized into subdirectories as: Music/Artist/Album/Artist - Title.mp3 (or .flac)
* Application runs of port 5000


## Deployment


```
GuessThatSong/run.py
```

## Built With

* [Flask](http://flask.pocoo.org/) - Web-development Framework

## Contributing

If you would like to contribute, please send a pull request against the master branch.


## Authors

* **Matt Murch** - *Initial work* - [Matt Murch](https://github.com/mattmurch)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
