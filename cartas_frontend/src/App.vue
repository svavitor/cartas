<script setup lang="ts">
import ListDecks from './components/ListDecks.vue';

</script>

<template>
  <main>
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
  width: 120px;
  margin: 5px;
}

body { 
  font-family: 'Roboto', sans-serif; 
} 

</style>
