# **Flute player with Raspberry Pi**

## **AUTHOR**

* Manel Lurbe Sempere (malursem@inf.upv.es)

## **DOCUMENTATION AND SET UP**

### **SOFTWARE REQUISITES**

- Install python3 for develop (Ubuntu/Debian based systems):

    ```sudo apt install python3-dev python3-pip python3-tk build-essential libi2c-dev i2c-tools libffi-dev```

- Install libs for python 3:

    ```sudo -H python3 -m pip install adafruit-circuitpython-busdevice adafruit-circuitpython-servokit adafruit-circuitpython-pca9685 PCA9685-driver RPi.GPIO wiringpi2```

### **HARDWARE REQUISITES**

- Raspberry Pi (any model) or other similar board with support of GPIO ports and python3. [Buy on amazon](https://www.amazon.es/s?k=raspberry+pi&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1)
- Cables to connect anything with the GPIO ports. [Buy on amazon](https://www.amazon.es/Neuftech-20cm-jumper-Arduino-Breadboard/dp/B00NBO4F76/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=gpio+cable+raspberry&qid=1582485107&s=toys&sr=1-2-catcorr)
- Servo motors. [Buy on amazon](https://www.amazon.es/gp/product/B07MPPF5CS/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- PCA9685 16 Channel PWM Servo Driver. [Buy on amazon](https://www.amazon.es/gp/product/B014KTSMLA/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)
- 1 Vent.
- 1 Flute.
- 1 Relé.

### **SET UP HARDWARE CONNECTIONS**

![](doc/images/gpio_flute.png)

### **HOW TO USE**

- Set execution permissions:

    ```chmod +x program.py```

- Usage:

     ```python3 program.py music_sheets/music_sheet.txt```

     or:

    ```./program.py music_sheets/music_sheet.txt```

**NOTE: Replace "program" with the name of the program you want to execute and "music_sheet" with the name of the song you want to play from the folder "music_sheets".**

### **MUSIC SHEETS**

<p align=justify>
I'm trying to find a lib or website that provides music sheets in plain text for bots or in more complex way, develop a machine learning algorithm to recognise notes in pdf or image based music sheets. The idea is to give the piano bot the capacity of play any kind of song without having to rewrite the music sheet specifically for him.
</p>

#### STYLE

Music Sheets for the piano are composed by a file of tuples (note,tempo), where "note" corresponds to the music note to be played and "tempo" the type of the note represented in the following table:

<table style="border:1px solid black;margin-left:auto;margin-right:auto;">
<tbody>
    <tr>
        <th>Music symbols</th>
        <th>Code Style</th>
    </tr>
    <tr>
        <td> &#119133; &#119133; </td>
        <td>dr</td>
    </tr>
    <tr>
        <td> &#119133; </td>
        <td>r</td>
    </tr>
    <tr>
        <td> &#119134; . </td>
        <td>b+</td>
    </tr>
    <tr>
        <td> &#119134; &#119136; </td>
        <td>b-</td>
    </tr>
    <tr>
        <td> &#119134; </td>
        <td>b</td>
    </tr>
    <tr>
        <td> &#119135; . </td>
        <td>n+</td>
    </tr>
    <tr>
        <td> &#119135; &#119136; </td>
        <td>n-</td>
    </tr>
    <tr>
        <td> &#119135; </td>
        <td>n</td>
    </tr>
    <tr>
        <td> &#119136; </td>
        <td>c</td>
    </tr>
    <tr>
        <td> &#119137; </td>
        <td>sc</td>
    </tr>
    <tr>
        <td> &#119139; </td>
        <td>ssc</td>
    </tr>
    <tr>
        <td> &#119140; </td>
        <td>sssc</td>
    </tr>
    <tr>
        <td> &#9837; </td>
        <td><i>*Write "b" after the note. Example: "mib" corresponds to note "mi flat".*<i></td>
    </tr>
    <tr>
        <td> &#9839; </td>
        <td><i>*Translate it to flats.*<i></td>
    </tr>
    <tr>
        <td> Silence </td>
        <td><i>*Same as the type of the note tempo. Example: "(sil,n)" corresponds to silence with the tempo of quarter note( &#119135; ).*<i></td>
    </tr>
</tbody>
</table>

In addition, you can play two or more notes at the same time if they have the same tempo in the same thread, separating them with a tab value key (\t). The file will be like this:

    do,n
    re,n
    mi,n
    fa,n
    sol,n
    la,n
    si,n
    do2,n