<template lang="html">
  <div class="container mt-4">
    <form class="form_poll" v-on:submit.prevent="sendPoll">
      <div id="wave">
        <h2 class="text-left pt-2 pl-4 text-white" style="z-index: 99;">Encuesta</h2>
      </div>
      <div class="mt-3 form_p d-flex flex-column">
        <div class="form-row">
          <div class="form-group col-md-12">
            <label for="email">Correo</label>
            <input type="email" class="form-control" id="email" v-model="email">
          </div>
          <div class="form-group col-md-6">
            <label for="edad">Edad</label>
            <select class="form-control" id="sexo" v-model="ageSelect" required>
              <option value="">&lt;Seleccione un Rango de Edad&gt;</option>
              <option v-for="age in ages" v-bind:key="age">{{age}}</option>
            </select>
          </div>
          <div class="form-group col-md-6">
            <label for="sexo">Sexo</label>
            <select class="form-control" id="sexo" v-model="sex" required>
              <option value="">&lt;Seleccione un Género&gt;</option>
              <option value="M">M</option>
              <option value="F">F</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label class="mb-3" for="networks">Selecciona tu Red Social Favorita</label>
          <div class="d-flex flex-wrap">
            <div class="form-check col-md-6 py-1 text-center" v-for="network in networks" v-bind:key="network.nombre" id="networks">
              <input class="form-check-input" type="radio" :value="network.nombre" v-model="netSelect">
              <label class="form-check-label" :for="network.nombre">
                {{ network.nombre }}
              </label>
              <label class="form-check-label" :for="network.nombre">
                <img :src="network.icono" width="25px" height="25px">
              </label>
            </div>
          </div>
        </div>
        <div class="form-group">
          <label class="mb-3">¿Cuanto tiempo en horas consumes en las siguientes redes sociales?</label>
          <div class="d-flex flex-wrap">
            <div class="col-md-6" v-for="(network, index) in networks" v-bind:key="network.nombre" id="time">
              <label for="number">Tiempo al día en {{network.nombre}}</label>
              <input type="number" min="0" max="24" class="form-control" id="time" value="0" v-model="timeSelect[index]" :key="index" required>
            </div>
          </div>
        </div>
        <button type="submit" class="btn btn_red px-3">Enviar Encuesta</button>
      </div>
    </form>
  </div>
</template>
<script>
// import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      networks: [
        { nombre: 'Facebook', icono: 'https://cdn-icons-png.flaticon.com/512/174/174848.png' },
        { nombre: 'WhatsApp', icono: 'https://cdn-icons-png.flaticon.com/512/134/134937.png' },
        { nombre: 'Twitter', icono: 'https://cdn-icons-png.flaticon.com/512/145/145812.png' },
        { nombre: 'Instagram', icono: 'https://cdn-icons-png.flaticon.com/512/2111/2111463.png' },
        { nombre: 'Tiktok', icono: 'https://cdn-icons-png.flaticon.com/512/3116/3116491.png' }
      ],
      ages: [ '18-25', '26-33', '34-40', '40+' ],
      ageSelect: '',
      netSelect: '',
      sex: '',
      email: '',
      timeSelect: []
    }
  },
  methods: {
    sendPoll () {
      var request = {
        correo: this.email,
        edad: this.ageSelect,
        sexo: this.sex,
        redsocialfav: this.netSelect,
        tfacebook: this.timeSelect[0],
        twhatsapp: this.timeSelect[1],
        ttwitter: this.timeSelect[2],
        tinstagram: this.timeSelect[3],
        ttiktok: this.timeSelect[4]
      }
      fetch('http://127.0.0.1:5000/add', {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(request), // data can be `string` or {object}!
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => this.$router.push({ path: '/table' }))
      // clear field
      this.email = ''
      this.ageSelect = ''
      this.sex = ''
      this.netSelect = false
      this.timeSelect[0] = ''
      this.timeSelect[1] = ''
      this.timeSelect[2] = ''
      this.timeSelect[3] = ''
      this.timeSelect[4] = ''
      request = {
        email: '',
        age: '',
        sex: '',
        favNetw: '',
        timeFacebook: '',
        timeWhatsApp: '',
        timeTwitter: '',
        timeInstagram: '',
        timeTiktok: ''
      }
    }
  },
  created () {
    // this.getMensaje()
  }
}

</script>
