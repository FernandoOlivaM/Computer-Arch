const express = require('express');
const mongoose = require('mongoose'); 
const Lab2 = require('./models/lab2')
const app = express()
const port = 3000

//variable de entorno
const uri = `mongodb+srv://admin:admin@cluster0.4enqq.mongodb.net/Arqui?retryWrites=true&w=majority`; 


mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(()=> console.log('conectado a mongodb')) 
  .catch(e => console.log('error de conexión', e))

const url = "https://localhost:44387/";

app.get("/guardar/:text",async (req, res) =>{
    const texto = req.params.text

    try {
        const nuevo = new Lab2()
        nuevo.fecha = Date()
        nuevo.texto = texto
        await nuevo.save()
        //respuesta al WIFI
        res.status(200).send("BITACORA FERNANDO OLIVA")

    } catch (error) {

        res.status(500).send()
    }
}
)

app.listen(port, () => console.log('ED2  escuchando en el puerto 3000'))
