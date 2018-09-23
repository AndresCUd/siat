package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.transmilenio.*
import com.google.firebase.firestore.FirebaseFirestore

class transmilenio: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.transmilenio)
        var xusuario=intent.getStringExtra("xusuario")

        B_menu.setOnClickListener {
            val i = Intent(this@transmilenio, menu::class.java)
            startActivity(i)
        }
        B_cerrar.setOnClickListener {
            val i = Intent(this@transmilenio, MainActivity::class.java)
            startActivity(i)
            val ref = FirebaseFirestore.getInstance().collection("usuarios").document(xusuario)
        }
        val db = FirebaseFirestore.getInstance().collection("estaciones")

        B_pnorte.setOnClickListener(){

            db.document("P.Norte").get().addOnSuccessListener {
            var q0=it.getString("8")!!
                var q1=it.getString("G11")!!
                var q2=it.getString("H74")!!
                var q3=it.getString("J72")!!
                T_bus1.setText("Bus 8")
                T_bus2.setText("bus G11")
                T_bus3.setText("bus H74")
                T_bus4.setText("busJ72")
                barra1.progress=Integer.parseInt (q0)
                barra2.progress=Integer.parseInt (q1)
                barra3.progress=Integer.parseInt(q2)
                barra4.progress=Integer.parseInt(q3)



            }
        }
    }



}
