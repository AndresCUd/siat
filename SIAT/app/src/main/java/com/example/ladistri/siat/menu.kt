package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.menu.*

class menu: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.menu)

        var xusuario=intent.getStringExtra("xusuario")

        B_transm.setOnClickListener {
            val i = Intent(this@menu, transmilenio::class.java)
            i.putExtra("xusuario", xusuario)
            startActivity(i)
        }
        B_sitp.setOnClickListener {
            val i = Intent(this@menu, sitp::class.java)
            i.putExtra("xusuario", xusuario)
            startActivity(i)
        }
        B_pagarqr.setOnClickListener {
            val i = Intent(this@menu, pagarqr::class.java)
            i.putExtra("xusuario", xusuario)
            startActivity(i)
        }
        B_info.setOnClickListener {
            val i = Intent(this@menu, info::class.java)
            i.putExtra("xusuario", xusuario)
            startActivity(i)
        }
        B_cuenta.setOnClickListener {
            val i = Intent(this@menu, cuenta::class.java)
            i.putExtra("xusuario", xusuario)
            startActivity(i)
        }
    }


}