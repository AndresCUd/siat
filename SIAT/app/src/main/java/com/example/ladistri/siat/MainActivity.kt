package com.example.ladistri.siat

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.ladistri.siat.R.id.contra
import com.example.ladistri.siat.R.id.usuario
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.QuerySnapshot
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {

    var xusuario = ""
    var xcontra = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        var s = ""
        var x = 0

        B_iniciar.setOnClickListener {
            x=0

            actualizar()
            //Se revisa si el usuario ya existe en la base de datos
            val ref = FirebaseFirestore.getInstance().collection("usuarios")


            ref.get().addOnCompleteListener { it ->
                for (document in it.result) {

                    if (document.id.equals(xusuario, ignoreCase = true)) {
                        x++

                    }
                }

                if (x == 1) {
                    val contradb = FirebaseFirestore.getInstance().collection("usuarios").document(xusuario)
                    contradb.get().addOnSuccessListener {
                        s = it.getString("contrasena")!!
                        if (x == 1 && s==xcontra ) {
                            val i = Intent(this@MainActivity, menu::class.java)
                            i.putExtra("xusuario", xusuario)

                            startActivity(i)
                            x=0
                            usuario.setText("")
                            contra.setText("")


                        } else {
                            Toast.makeText(this, "usuario o contrasena invalidos", Toast.LENGTH_LONG).show()
                            x=0

                        }
                    }

                }




            }



        }
        B_registrarse.setOnClickListener {
            val i = Intent(this@MainActivity, registro::class.java)
            startActivity(i)
        }
    }



    fun actualizar() {
        xusuario = usuario.text.toString()
        xcontra = contra.text.toString()
    }
}













