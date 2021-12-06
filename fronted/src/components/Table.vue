<template lang="html">
    <div class="container w-100 h-100">
      <div class="mt-5 mx-auto d-flex flex-column">
        <h2 class="text-center">Graicas por realizar nuestra encuesta <img src="https://images.emojiterra.com/google/android-10/512px/1f44b.png" width="40px" height="40px"></h2>
        <div class="row justify-content-center align-items-center d-flex flex-column" role="alert">
          <p class="text-center p-4">Puedes vizualizar los resultados de las encuestas hasta ahora en la siguiente tabla</p>
          <div class="d-flex flex-wrap w-100 border_round">
            <div class="text-center bg_red w-100">
              <h2 class="text-center text-white">Tabla de Resultados de las Encuestas</h2>
            </div>
            <div class="d-flex flex-wrap col-12 border border-danger bg_gray">
              <label>Cantidad de encuestas respondidas:</label>
              <p class="ml-1 mb-0">{{questions.length}}</p>
            </div>
            <div class="d-flex flex-column col-12 border border-danger">
              <label>Tiempo promedio por red social:</label>
              <div class="d-flex flex-column">
                <p class="ml-1 mb-0">Facebook: {{mediaRed.tfacebook}} h</p>
                <p class="ml-1 mb-0">WhatsApp: {{mediaRed.twhatsapp}} h</p>
                <p class="ml-1 mb-0">Twitter: {{mediaRed.ttwitter}} h</p>
                <p class="ml-1 mb-0">Instagram: {{mediaRed.tinstagram}} h</p>
                <p class="ml-1 mb-0">Tiktok: {{mediaRed.ttiktok}} h</p>
              </div>
            </div>
            <div class="d-flex flex-wrap col-12 bg_gray px-0">
              <div class="col-md-6 d-flex flex-nowrap border border-danger">
                <label>Red Social Favorita:</label>
                <p class="ml-1 mb-0">
                  <span v-for="(item, index) in favorite" :key="index">
                    {{item}}{{(index !== favorite.length - 1) ? ',' : ''}}
                  </span>
                </p>
              </div>
              <div class="col-md-6 d-flex flex-nowrap border border-danger">
                <label>Red Social Menos Querida:</label>
                <p class="ml-1 mb-0">
                  <span v-for="(item, index) in noFavorite" :key="index">
                    {{item}}{{(index !== noFavorite.length - 1) ? ',' : ''}}
                  </span>
                </p>
              </div>
            </div>
            <div class="d-flex flex-column col-12 border border-danger">
              <label>Rango de edad que más usa cada red social:</label>
              <div class="d-flex flex-column">
                <p class="ml-1 mb-0">Facebook: 
                  <span v-for="(item, index) in yearsUses.Facebook" :key="index">
                    {{item}}{{(index !== yearsUses.Facebook.length - 1) ? ',' : ''}}
                  </span>
                </p>
                <p class="ml-1 mb-0">WhatsApp:
                  <span v-for="(item, index) in yearsUses.WhatsApp" :key="index">
                    {{item}}{{(index !== yearsUses.WhatsApp.length - 1) ? ',' : ''}}
                  </span>
                </p>
                <p class="ml-1 mb-0">Twitter: 
                  <span v-for="(item, index) in yearsUses.Twitter" :key="index">
                    {{item}}{{(index !== yearsUses.Twitter.length - 1) ? ',' : ''}}
                  </span>
                </p>
                <p class="ml-1 mb-0">Instagram: 
                  <span v-for="(item, index) in yearsUses.Instagram" :key="index">
                    {{item}}{{(index !== yearsUses.Instagram.length - 1) ? ',' : ''}}
                  </span>
                </p>
                <p class="ml-1 mb-0">Tiktok: 
                  <span v-for="(item, index) in yearsUses.Tiktok" :key="index">
                    {{item}}{{(index !== yearsUses.Tiktok.length - 1) ? ',' : ''}}
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="d-flex flex-wrap">
          <router-link to="/" tag="button" class="mt-4 btn btn_red px-4 mx-auto">Volver al inicio</router-link>
          <router-link to="/poll" tag="button" class="mt-4 btn btn_red px-4 mx-auto">Volver a realizar la encuesta</router-link>
        </div>
      </div>
    </div>
</template>

<script>
// scrips
export default {
  name: 'Main',
  data () {
    return {
      yearsUse: [
        '18-25',
        '26-33',
        '34-40',
        '40+'
      ],
      redUses: {
        Facebook: '18-25',
        WhatsApp: '18-25',
        Twitter: '18-25',
        Instagram: '18-25',
        Tiktok: '18-25'
      },
      redsUses: {
        Facebook: {
          '18-25': 0,
          '26-33': 0,
          '34-40': 0,
          '40+': 0
        },
        WhatsApp: {
          '18-25': 0,
          '26-33': 0,
          '34-40': 0,
          '40+': 0
        },
        Twitter: {
          '18-25': 0,
          '26-33': 0,
          '34-40': 0,
          '40+': 0
        },
        Instagram: {
          '18-25': 0,
          '26-33': 0,
          '34-40': 0,
          '40+': 0
        },
        Tiktok: {
          '18-25': 0,
          '26-33': 0,
          '34-40': 0,
          '40+': 0
        }
      },
      hoursReds: {
        tfacebook: 0,
        ttiktok: 0,
        ttwitter: 0,
        tinstagram: 0,
        twhatsapp: 0
      },
      socialReds: {
        Facebook: 0,
        WhatsApp: 0,
        Twitter: 0,
        Instagram: 0,
        Tiktok: 0
      }
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    async getData () {
      await this.$store.dispatch('main/get')
    },
    reset (myKey, keys) {
      keys.map( (key) => {
        this[myKey][key] = 0
      })
    }
  },
  computed: {
    questions: {
      get () {
        return this.$store.getters['main/getQuestions']
      }
    },
    mediaRed () {
      this.reset('hoursReds', ['tfacebook', 'ttiktok', 'ttwitter', 'tinstagram', 'twhatsapp'])
      this.questions.map((question) => {
        for (const key in this.hoursReds) {
            this.hoursReds[key] += question[key]
        }
      })

      for (const key in this.hoursReds) {
        this.hoursReds[key] = this.hoursReds[key]/this.questions.length
        this.hoursReds[key] = this.hoursReds[key].toFixed(2)
      }

      return this.hoursReds
    },
    pointsRed () {
      this.reset('socialReds', ['Facebook', 'WhatsApp', 'Twitter', 'Instagram', 'Tiktok'])
      this.questions.map((question) => {
        for (const key in this.socialReds) {
          if (
            Object.hasOwnProperty.call(question, 'redsocialfav') &&
            question.redsocialfav === key
          ) {
            this.socialReds[key]++
          }
        }
      })
      return this.socialReds
    },
    favorite () {
      let old = 0;
      let allKeys = ['']
      for (const key in this.pointsRed) {
        if(this.pointsRed[key] > old){
          allKeys = ['']
          old = this.pointsRed[key]
          allKeys[0] = key
        }else if(this.pointsRed[key] === old){
          old = this.pointsRed[key]
          allKeys.push(key)
        }
      }

      return allKeys
    },
    noFavorite () {
      let old = Infinity
      let allKeys = ['']
      for (const key in this.pointsRed) {
        if(this.pointsRed[key] < old){
          allKeys = ['']
          old = this.pointsRed[key]
          allKeys[0] = key
        }else if(this.pointsRed[key] === old){
          old = this.pointsRed[key]
          allKeys.push(key)
        }
      }

      return allKeys
    },
    yearsUses () {
      this.reset('yearsUse', ['18-25', '26-33', '34-40', '40+'])
      this.questions.map((question) => {
        this.yearsUse.map( (item) => {
           if (
            Object.hasOwnProperty.call(question, 'edad') &&
            question.edad === item
          ) {
            this.redsUses[question.redsocialfav][item]++
          }
        })
      })

      for (const key0 in this.redsUses) {
        let old = 0
        let myKeys = []
        for (const key in this.redsUses[key0]) {
          if(this.redsUses[key0][key] > old){
            myKeys = []
            old = this.redsUses[key0][key]
            myKeys[0] = key
          }else if(this.redsUses[key0][key] === old){
            old = this.redsUses[key0][key]
            myKeys.push(key)
          }
        }
        if(old !== 0) this.redUses[key0] = myKeys
        else this.redUses[key0] = '0'
      }
      return this.redUses
    }
  }
}
</script>

<style type="text/css" scoped>
  label{
    margin: 0px
  }
</style>
