<template lang="html">
    <div class="container d-flex h-100">
      <div class="mt-5">
        <h2 class="text-center">Bienvenido!! <img src="https://images.emojiterra.com/google/android-10/512px/1f44b.png" width="40px" height="40px"></h2>
        <div class="row justify-content-center align-items-center d-flex flex-column" role="alert">
          <p class="text-center p-4">
            Estamos realizando una investigación sobre el uso de <b>redes sociales</b>. Nos gustaría saber qué tipo de redes utilizas con mayor frecuencia y cual de ellas es tu favorita. Esto nos ayudará a hacer mejoras en las herramientas actuales y a dar prioridad a nuevas funciones. Las respuesta de los particiantes podra ser consultada al terminer la encuesta.
          </p>
          <router-link to="/poll" tag="button" class="btn btn_red px-3">Participar</router-link>
          <div style="height: 400px; margin-top: 6.7rem;">
            <img src="https://vilmanunez.com/wp-content/uploads/2020/04/li%CC%81mite-de-caracteres-redes-sociales.png" width="100%" height="100%">
          </div>
        </div>
      </div>
    </div>
</template>
<script>
// import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      mensaje: 'Nuevo mensaje desde Vue.js'
    }
  },
  methods: {
    // getMensaje () {
    //   const path = 'http://127.0.0.1:5000/api/v.1/mensaje'
    //   axios.get(path).then((respuesta) => {
    //     this.mensaje = respuesta.data
    //   })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // }
  },
  created () {
    // this.getMensaje()
  }
}

</script>
<style lang="css" scoped>

</style>
