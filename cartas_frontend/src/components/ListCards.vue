<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

interface Card {
  front: string,
  back: string,
  review_count: number,
  review_multiplier: number,
  last_review: any,
  next_review: any
}

const cards = ref([] as Card[])
const props = defineProps(['deck_id'])
const current_card = ref()
const current_card_index = ref(0)
const front_text = ref('')
const back_text = ref('')
const is_answer_visible = ref(false)

async function load_cards() {
  const cards_by_deck = await axios.get<Card[]>('http://127.0.0.1:8081/cards/by-deck/'+ props.deck_id)
  cards.value = cards_by_deck.data
  current_card.value = cards.value[current_card_index.value]
}

function next_card(){
    is_answer_visible.value = false
  if (current_card_index.value < cards.value.length) {
    current_card_index.value += 1
    current_card.value = cards.value[current_card_index.value]
  } else {
    current_card.value = null
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

function toggle_answer(){
    is_answer_visible.value = !is_answer_visible.value
}

async function create_card(){
  await axios.post('http://127.0.0.1:8081/cards/', {
    front: front_text.value,
    back: back_text.value,
    deck: props.deck_id
  })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('Erro ao criar carta:', error)
      })
}

watch(props, async () => { await load_cards() })

onMounted(async () => {
  await load_cards()  
})

</script>

<template>
  <main>
    <p>Cards to review: {{ cards.length - current_card_index }}</p>

    <div class="current_card" v-if="current_card" @click="toggle_answer">
      <div class="front" v-if="!is_answer_visible">
        <p>{{ current_card?.front }}</p>
      </div>
      <div class="back" v-if="is_answer_visible">
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
