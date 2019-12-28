# Japanese OCR in Python

## Dependencies

- Python 3
- OpenCV >= 4
- Tesseract (see below)

### Tesseract

- Install `tesseract` 4.0
- Download `jpn_vert.traineddata` [here](https://github.com/tesseract-ocr/tessdata/blob/master/jpn_vert.traineddata)
- Copy `jpn_vert.traineddata` in `/usr/share/tessdata`
- Check with `tesseract --list-langs` that `jpn_vert` correctly appears

### Archlinux

```

pacman -S opencv tesseract-ocr-git tesseract-data-jpn
```

### Ubuntu / Mint

```
sudo apt-get install -y tesseract-ocr tesseract-ocr-jpn-vert
sudo apt-get install -y python3-opencv
```

## How to use

The code should susuccessfully run on Linux.Currently I am using WSL Ubuntu 18.04.
Put every pictures in `picutures`, then run
```
python main.py
```

Then you should get every pages in `allresult`

## How to setup

```

sudo apt install tesseract-ocr

pip3 install scipy

pip3 install opencv-python

 sudo apt-get install language-pack-ja language-pack-gnome-ja language-pack-ja-base language-pack-gnome-ja-base

 ```
notice that the path for tessdata is now `/usr/share/tesseract-ocr/tessdata`
