package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.info.*

class info: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.info)

        B_menu.setOnClickListener {
            val i = Intent(this@info, menu::class.java)
            startActivity(i)
        }
        B_cerrar.setOnClickListener {
            val i = Intent(this@info, MainActivity::class.java)
            startActivity(i)
        }
    }
}