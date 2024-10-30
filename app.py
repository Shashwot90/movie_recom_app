import streamlit as st 
import pickle 
import pandas as pd 
import requests

# Counting objects: 100% (9/9), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (8/8), done.
# Writing objects: 100% (8/8), 46.36 MiB | 1.98 MiB/s, done.
# Total 8 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (3/3), completed with 1 local object.
# remote: error: Trace: 6c2629e8ace05b9b129730cd74828ed13624ddf8b20f643bebc7138e4f61ae90
# remote: error: See https://gh.io/lfs for more information.
# remote: error: File similarity.pkl is 176.22 MB; this exceeds GitHub's file size limit of 100.00 MB
# remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
# To https://github.com/Shashwot90/movie-recommendation-system.git
#  ! [remote rejected] main -> main (pre-receive hook declined)
# error: failed to push some refs to 'https://github.com/Shashwot90/movie-recommendation-system.git'