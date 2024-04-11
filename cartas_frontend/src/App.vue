<script setup lang="ts">
import { ref, onMounted } from 'vue'
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
const current_card = ref()
const current_card_index = ref(0)

async function loadCards() {
  const listCards = await axios.get<Card[]>('http://127.0.0.1:8081/cards/')
  cards.value = listCards.data
  current_card.value = cards.value[current_card_index.value]
}
function next_card(){
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

onMounted(async () => {
  await loadCards()  
})

</script>

<template>
  <main>
    <p>Cards to review: {{ cards.length - current_card_index }}</p>

    <div class="current_card" v-if="current_card">
      <p>{{ current_card?.front }}</p>
      <p>{{ current_card?.back }}</p>
    </div>

    <div class="current_card" v-else="current_card">
      <p>No more Cards to review.</p>
    </div>

    <button class="c-button" @click="call_x">X</button>
    <button class="c-button" @click="call_o">O</button>
  </main>
</template>

<style scoped>

.current_card {
  background-color: rgb(75, 54, 37);
  border: solid 1px rgb(3, 3, 3);
  height: 300px;
  width: 230px;
  margin: 5px;
  padding-top: 50px;
  text-align: center;
}

button {
  width: 110px;
  margin: 5px;
}

</style>
