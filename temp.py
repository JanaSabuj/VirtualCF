import os
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

dex_x = ['A', 'B', 'C', 'D', 'E']
dev_y = [21,25,11,82,55]

plt.plot(dex_x, dev_y)
plt.savefig('foo.png')


