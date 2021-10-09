const mongoose = require('mongoose');
const Scheema = mongoose.Schema

const lab2Scheema = new Scheema({
    texto: String,
    fecha: Date
})
const Lab2 = mongoose.model('Lab2', lab2Scheema)

module.exports = Lab2




