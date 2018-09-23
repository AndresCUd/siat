package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.cuenta.*

class cuenta: AppCompatActivity() {
    var incedula=""
    var innombre=""
    var inncorreo=""
    var inntelefono=""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.cuenta)

        var xusuario=intent.getStringExtra("xusuario")
        val contradb = FirebaseFirestore.getInstance().collection("usuarios").document(xusuario)
        contradb.get().addOnSuccessListener {
            incedula= it.getString("cedula")!!
            innombre= it.getString("nombre")!!
            inncorreo= it.getString("correo")!!
            inntelefono=  it.getString("telefono")!!
            actualizar()
        }


        B_menu.setOnClickListener {
            val i = Intent(this@cuenta, menu::class.java)
            startActivity(i)
        }
        B_cerrar.setOnClickListener {
            val i = Intent(this@cuenta, MainActivity::class.java)
            startActivity(i)
        }
    }

    fun actualizar() {
        T_usuario.text=innombre
        T_telefono.text=inntelefono
        T_correo.text=inncorreo
        T_cedulaa.text=incedula
    }


}
