# CSE464--MCQ Corrector

This repo contains the solution to the MCQ Corrector Kaggle Competition. The competition is about designing an image processing pipeline to automatically correct the scanned documents for students answers. You can find this competition right [here](https://www.kaggle.com/c/cse-464-mcqcorrector).

In this competition, there were 52 teams competing. And my team's solution ranked the first.

![The Competition Leaderboard](http://www.mediafire.com/convkey/85e1/f00rd2wzejcl33ezg.jpg)



# Challenge

Manually correcting a huge amount of data is a very time-consuming task, also creating an intelligent system without being 100% accurate won't be a usable solution, as we can't accept that a student doesn't get what he/she deserves, that's why we're not targeting only high accuracy, but we're targeting a perfect solution.

The challenges you'll face during building your automatic solution are usually due to students not following the rules:

- They are required to use a 2B Pen, but some students use a lighter pen:


- They're required to fully fill the circle of the answer, but some students just don't:


- They're required to have only one answer per question, but some students just don't, so this should be considered a mistake even if any of the two filled answers is correct:


- They're required to use the same fill level all over the answer sheet, but you'll find someone who doesn't fill the circles consistently across his/her answer sheet:


- They're required that if they changed their answers, they should erase the mistake completely, but some don't fully erase it, though this case should be considered as a correct answer if the black answer is correct if and only if there's a clear difference between intensity levels of the marked answers like in Q35 answers:


- They're required not to do anything in the answer sheet except only filling the circles, but you'll find some random noise in the answer sheet apparently due to the eraser, also they may leave a question not answered, though they may have a chance randomly getting it correct:


- Last challenge is the scanning process, which doesn't align the images vertically, so you may find a scanned image slightly rotated to the right or left, you'll need to handle this in your preprocessing system.

These are mainly the challenges that you'll need to handle while building your correction algorithm.

