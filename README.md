# Prerequisites

## Linux

Just install [Gentoo](http://gentoo.org).

## Inkscape

Install it with postscript support. On Gentoo:

```
# euse --package media-gfx/inkscape --enable postscript
# emerge media-gfx/inkscape
```

## Python

Install python3 and requirements. On Gentoo:

```
# emerge ">dev-lang/python-3"
```

and then requirements:

```
$ pip3 install --user --requirements requirements.txt
```

## Texlive

On Gentoo:

```
# euse --package app-text/texlive --enable graphics
# euse --package app-text/texlive --enable xetex
# emerge app-text/texlive
```

# Make it

```
$ make
```

Remember to read Makefile output and update:

- `all.tex`

- `generate_input.py`

- `contacts.py`

- `graphics/*.svg`

# Notes

## eps files

`graphics/*.eps` are automatically generated. Don't even try to edit them, most probably your effort will be quickly lost.

## Fonts

You may want to install CasablancaAntique font from `fonts/` directory. It even supports Ń and ń characters.

## Bugs

Pull requests are welcome.
