# Obey The Testing Goat - 21st August 2022


# Branch first.. Basic Git commands

How to Clone? (get a fresh repository in local box)
```
git clone git@github.com:kanchiraghuraman/ottg.git
```

How to branch?

```
git checkout -b users/ini/20220821_prerequisites
```

Save changes
```
git add -A
git commit -am "Some context message"
```

Send changes to repository
```
git push --set-upstream origin users/ini/20220821_prerequisites
```


# Lesson 00: Prerequisites

Install python

mkdir /src/learning/YYYYMM

```
mkdir /src/learning/202208

mkdir /src/learning/202208/ottg

cd /src/learning/202208/ottg

git init

code .
```

# Setup python virtual environment

Ensure you are in the correct folder/directory.
```
python -m venv venv

```