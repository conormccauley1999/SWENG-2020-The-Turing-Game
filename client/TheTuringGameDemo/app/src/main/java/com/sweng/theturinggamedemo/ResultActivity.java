package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import java.util.Objects;

public class ResultActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);
        Objects.requireNonNull(getSupportActionBar()).hide();

        findViewById(R.id.result_button_menu).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(ResultActivity.this, MainActivity.class));
            }
        });

        findViewById(R.id.result_button_survey).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(ResultActivity.this, SurveyActivity.class));
            }
        });

    }

    @Override
    protected void onStart() {

        super.onStart();

        // If the user guessed correctly show the 'correct' image, otherwise show the 'incorrect' image
        if (Globals.guessResult) {
            findViewById(R.id.result_image_correct).setVisibility(View.VISIBLE);
        } else {
            findViewById(R.id.result_image_incorrect).setVisibility(View.VISIBLE);
        }

    }

}
