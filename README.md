# pasta-python
Project that uses a raspberry pi zero w 2 and a Gy-mlx90614-dci Long-distance infrared sensor

I made this app to alert me when my pasta water is boiling. All so I can step away for a few minutes while the water comes to boil.

The temperature used to alert me has been fine tuned to my location (altitude) and preference (I like to get back as it's coming to boil)

For push notifications to my phone I use pushsafer which is a paid service up to how many tokens you wish to buy. You can essentially get a lifetime supply for about 10 dollars. (Feel free to replace my solution with any alternative you see fit)

![image](https://user-images.githubusercontent.com/65210276/186677683-34d82c07-2db2-4856-b0a8-c2b6487e17b1.png)

Above you'll find the psuedo-headless configuration used in this project. It hangs above the stove at an angle at least within 2 feet of the stove top it's measuring.

There is a limit on distance as the IR sensor takes the average of everything it can see, but you can take some liberties with this limitation in mind.

Finding the right trigger temperature is key as the sensor, while more than a foot away, can be off by 5 or so degrees. If we account for this in the code, realistically there is no issue as long as your sensor is able to consistently reach that temperature while you are boiling water.
