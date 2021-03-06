// Class worked on by the AI Group: Claire McNamara, Diego Molamphy

package com.sweng.theturinggame;

import java.util.Random;

public class Adult extends BotPersonality {

    public int age, probSpellingMistake;

    public Adult(String name){
        super(name);
        Random rand = new Random();
        this.age = rand.nextInt((40 - 29) + 1) + 29;
        this.probSpellingMistake = rand.nextInt((7 - 5) + 1) + 5;
    }

    @Override
    public String addPersonality(String input){
        return input;
    }
}
