<template>
  <UApp>
    <Navigation />
    <NuxtPage />
  </UApp>
</template>

<script setup lang="ts">
import Navigation from './components/Navigation.vue'
import type UserInfo from './types/UserInfo'


// interfaces


// varibles
const authUri = {
  dev: 'https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fauthorize&scope=identify+guilds+guilds.join+email',
  prod: 'https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=https%3A%2F%2Fnhdiscord.com%2Fauthorize&scope=identify+guilds+guilds.join+email'
}.prod

const appUri = {
  dev: 'http://localhost:8000',
  prod: 'https://api.nhdiscord.com'
}.prod

// refs
const userInfo = ref<UserInfo>({
  username:undefined,
  avatar:undefined
})

// provides
provide('authUri', authUri)
provide('appUri', appUri)
provide('userInfo', userInfo)

// methods
onMounted(async () => {
  const web_token = localStorage.getItem('web_token')
  if (web_token) {
    userInfo.value.username = localStorage.getItem('username')!
    userInfo.value.avatar = localStorage.getItem('avatar')!
  }
})

</script>