<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ListDecks from './components/ListDecks.vue';
import { hasJSDocParameterTags } from 'typescript';

interface Card {
  front: string,
  back: string,
  review_count: number,
  review_multiplier: number,
  last_review: any,
  next_review: any
}

const cards = ref([] as Card[])
const current_card = ref()
const current_card_index = ref(0)
const front_text = ref('')
const back_text = ref('')
const card_div = ref(true)

async function loadCards() {
  const listCards = await axios.get<Card[]>('http://127.0.0.1:8081/cards/')
  cards.value = listCards.data
  current_card.value = cards.value[current_card_index.value]
}

function next_card(){
  card_div.value = true
  if (current_card_index.value < cards.value.length) {
    current_card_index.value += 1
    current_card.value = cards.value[current_card_index.value]
  } else {
    current_card.value = null
    console.log('No more cards.')
  }
}

function call_x(){
  next_card()
  console.log("X")
}

function call_o(){
  next_card()
  console.log("O")
}

function toggle_card(){
  card_div.value = !card_div.value
}

async function create_card(){
  await axios.post('http://127.0.0.1:8081/cards/', {
    front: front_text.value,
    back: back_text.value,
    deck: 1
  })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('Erro ao criar carta:', error)
      })
}

onMounted(async () => {
  await loadCards()  
})

</script>

<template>
  <main>
    <p>Cards to review: {{ cards.length - current_card_index }}</p>

    <div class="current_card" v-if="current_card" @click="toggle_card">
      <div class="front" v-if="card_div">
        <p>{{ current_card?.front }}</p>
      </div>
      <div class="back" v-if="!card_div">
        <p>{{ current_card?.front }}</p>
        <hr>
        <p>{{ current_card?.back }}</p>
      </div>
    </div>

    <div class="current_card" v-else="current_card">
      <p>No more Cards to review.</p>
    </div>
    <button class="c-button" @click="call_x">X</button>
    <button class="c-button" @click="call_o">O</button>

    <hr> <br>

    <label>Front: </label> <br>
    <textarea v-model="front_text" rows="4" cols="50"> </textarea> <br>

    <label>Back: </label> <br>
    <textarea v-model="back_text" rows="4" cols="50"> </textarea> <br>

    <button class="c-button" @click="create_card">Criar carta</button>
     
    <hr>
    <ListDecks></ListDecks>
  </main>
</template>

<style scoped>

.current_card {
  background-color: rgb(180, 178, 177);
  border: solid 1px rgb(3, 3, 3);
  height: 500px;
  width: 600px;
  margin: 5px;
  padding: 50px 20px 20px 20px;

  text-align: center;
}

button {
  width: 316px;
  margin: 5px;
}

</style>
