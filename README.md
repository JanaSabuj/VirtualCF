# VirtualCF
A Codeforces parser for a specific contest identified by **contest-id**. Can be used for uninterrupted and smooth participation in a virtual contest, upsolving a practice contest or even a live contest.

**Inspiration** 
> Python is the "most powerful language you can still read".

# What it does
* You are prompted the contest-id of the Codeforces contest you want to upsolve
    * You **enter** the contest-id
* You are prompted for the preferred coding language from a list of options
    * You **enter** the option no.
* The script starts scraping the desired contest
* A Folder is created having the format ( name-of-the-contest)
    * Each folder has individual folders for each problem (A to F)
        * Each such sub-folder has 3 files (Assuming the problem is A)
            * A.cpp (Assuming you code in cpp)
            * A.txt (The i/o file)
            * input.txt 
    * A stats.txt and a stats.png file is also created having showing the problem vs accepted ratio.It helps the user gauge the difficulty of each problem and the contest as a whole.

# What to do
* Star the repo and clone it.
* Download all the files in a zip 
* Install latest version of python (add to PATH) if not already installed
* **Pip install** all the **below mentioned modules** and dependencies
* Place the script in a folder where you want the folder of the contest
* Place your code template inside the **template.txt** file
* Run **python3 vir.py** or **python vir.py** as suitable
* **Bonus** - If you place it in a **git initialised repository**, after the script finishes, you can simply commit all the changes and all your contest-codes will be pushed to github
* An active internet connection while the script parses     

# Youtube demo
<!-- [My first youtube tutorial](https://youtu.be/bci2ogajpFI) -->

# The contest we want to participate in
![1](https://user-images.githubusercontent.com/39147514/65833571-5f925f00-e2ef-11e9-9387-bec6c396ab20.png)

# Starter code to be placed in template.txt (I have used my personal template in repo)

```
 int main() {
	// your code goes here
	freopen("input.txt", "r" , stdin);
	return 0;
 }
 
```
# The highlighted part is the contest-id
![1](https://user-images.githubusercontent.com/39147514/65833821-08da5480-e2f2-11e9-8180-ffd731417d9a.png)

# Script prompting for contest-id and the preferred language choice
![1](https://user-images.githubusercontent.com/39147514/65833833-31fae500-e2f2-11e9-880c-6383cb78cb17.png)

# Start of file parsing ( has created the contest-folder)
![1](https://user-images.githubusercontent.com/39147514/65833871-9fa71100-e2f2-11e9-9421-84a4723d9b61.png)

# Middle of parsing (inside the parent folder.. **A** problem has been scraped )
![1](https://user-images.githubusercontent.com/39147514/65833898-f3195f00-e2f2-11e9-934f-efe00230829c.png)

# Middle of parsing (inside the parent folder.. **B** problem has been scraped )
![1](https://user-images.githubusercontent.com/39147514/65833907-1ba15900-e2f3-11e9-98b0-a8053c898214.png)

# Middle of parsing (inside the parent folder.. **F** problem has also been scraped )
![1](https://user-images.githubusercontent.com/39147514/65833918-3e337200-e2f3-11e9-8b40-d81851474465.png)

# Stats.png and stats.txt has been generated
![1](https://user-images.githubusercontent.com/39147514/65833929-5b684080-e2f3-11e9-99d1-d2689f600022.png)

# stats.png
![1](https://user-images.githubusercontent.com/39147514/65833936-7aff6900-e2f3-11e9-9fcb-98bd7d07cf6f.png)

# Peek inside the directory structure of a contest
![1](https://user-images.githubusercontent.com/39147514/65833943-92d6ed00-e2f3-11e9-8259-cbeb47bd8dd3.png)

# A.txt
![1](https://user-images.githubusercontent.com/39147514/65833951-aa15da80-e2f3-11e9-835b-c00cf6fd5e51.png)

# A.cpp (with a generic starter file)
![1](https://user-images.githubusercontent.com/39147514/65833957-c6197c00-e2f3-11e9-8e46-f634657b93e1.png)

### Some users may encounter a https error. Here's the walkthrough.
You need to change all the **https** to **http** and delete the argument **verify = True** from every get request.
![verify-true-git](https://user-images.githubusercontent.com/39147514/65818085-cc442580-e22b-11e9-8e05-bd04eadb6965.png)

The highlighted parts show the https and verify=True clauses. They need to be dealt with as described above the pic.

## Requirements
* Modules
    * os
    * sys
    * requests
    * re
    * bs4 (BeautifulSoup)
    * time
    * matplotlib

* User Requiremets
    * codeforces-contest-id of any contest

* Python Version
    * 3 or above

* Active internet when py - script runs

* The terminal (required for input) shows log as the script runs


