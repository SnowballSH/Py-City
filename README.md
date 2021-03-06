# Py-City
### 3D visualization for Python projects

With this project, you can analyze and view your 
python github repositories in a different way!

![example - snow lang](https://cdn.discordapp.com/attachments/597175122222252038/791432562429263872/unknown.png)

---

## How to run:

```shell script
git clone https://github.com/SnowballSH/Py-City
cd Py-City # or whatever the name of the folder cloned
pip install -r requirements.txt
python main.py
```

### You will be likely to see a window pop up

(Wait a few seconds patiently, because the program needs to pull the repo)

### Hold the right click of your mouse to rotate the scene!!

Make sure you are in the root directory of Py-City!

#### The current main.py lets you view the [source repo](https://github.com/SnowballSH/Snow-lang) of **the Snow Programming Language**
(Which I made myself)

#### If you want to analyze another repo, change main.py to
```python
from src.main_analyze import analyze, display

if __name__ == "__main__":
    data = analyze("YOUR_REPO_LINK")
    display(data)
```

(Make sure it is a valid link or the program will abort)

## Have fun!
