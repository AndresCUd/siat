package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.pagarqr.*


class pagarqr: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.pagarqr)

        B_menu.setOnClickListener {
            val i = Intent(this@pagarqr, menu::class.java)
            startActivity(i)
        }
        B_cerrar.setOnClickListener {
            val i = Intent(this@pagarqr, MainActivity::class.java)
            startActivity(i)
        }
    }


}