Lyrics learner helps you memorize lyrics.

## Usage

```
python learn.py "my-lyrics.txt"
```

Lyrics text files must be in the same directory as `learn.py`.

### Verses

It can be useful to focus on a particular verse of the song. If you separate
the verses in the text file by `---`, `learn` will ask you which verses
you want to learn and you can select one or several.

```
First line 
Second line

---

First line of the second verse
Second line of the second verse
```


### Lines

You can tweak the number of lines shown after the random line shown by passing
the `--nb-lines` argument. 
