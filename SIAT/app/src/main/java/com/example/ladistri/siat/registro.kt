package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.registro.*

class registro : AppCompatActivity() {
   var datos=datospersona()


    override fun onCreate(savedInstanceState: Bundle?) {
        val dbusuarios = FirebaseFirestore.getInstance().collection("usuarios")
        super.onCreate(savedInstanceState)
        setContentView(R.layout.registro)
        B_finalizar.setOnClickListener {

            if(condicion()==0){
            actualizardatos()
            borrarcampos()
         dbusuarios.document(datos.cedu).set(mapOf(
                 "cedula" to datos.cedu,
         "contrasena"  to datos.contrasena,
                 "correo" to datos.correo,
                 "debito" to datos.debito,
                 "nombre" to datos.nombre,
                 "telefono" to datos.telefono,
                 "tipo" to datos.tipo

         ))
            val i = Intent(this@registro, MainActivity::class.java)
            startActivity(i)}else{

                Toast.makeText(this, "rellena los campos.", Toast.LENGTH_LONG).show()
            }
        }
    }

    fun actualizardatos() {
        datos.cedu= T_cedula.text.toString()
        datos.contrasena=T_contra.text.toString()
        datos.debito=T_cuentadebito.text.toString()
        datos.correo=T_correo.text.toString()
        datos.nombre=T_usuario.text.toString()
        datos.telefono=T_telefono.text.toString()
        datos.tipo="usuario"
        datos.saldo="0"
    }
    fun borrarcampos() {
        T_cedula.setText("")
        T_contra.setText("")
        T_cuentadebito.setText("")
        T_correo.setText("")
        T_usuario.setText("")
        T_telefono.setText("")
    }

    fun condicion(): Int {
        var x=0
        if(T_telefono.text.toString().isEmpty() ||T_usuario.text.toString().isEmpty() ||T_correo.text.toString().isEmpty() ||T_cedula.text.toString().isEmpty() ||T_cuentadebito.text.toString().isEmpty() ||T_contra.text.toString().isEmpty() ){
            x++

        }
        return x
    }


}
