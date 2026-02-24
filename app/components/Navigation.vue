<template>
    <UHeader>
        <template #title>
            <Logo class="h-12" />
        </template>
        <UNavigationMenu :items="items"/>

        <template #body>
            <UNavigationMenu orientation="vertical" :items="items"/>
        </template>

        <template #right>
            <UButton v-if="!userInfo.username" icon="ic:baseline-discord" class="bg-[#5865F2] text-[#E0E3FF]">Login</UButton>
            <UDropdownMenu :items="userOptions">
                <UButton :avatar="{src:userInfo.avatar}" variant="subtle" color="neutral"  >{{ userInfo.username }}</UButton>
            </UDropdownMenu>
            
        </template>
    </UHeader>
</template>

<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'
import type { DropdownMenuItem } from '@nuxt/ui'
import Logo from './Logo.vue';
import type UserInfo from '~/types/UserInfo'

// injects
const userInfo = inject<Ref<UserInfo>>('userInfo')!

// refs

const userOptions = ref<DropdownMenuItem[]>([
    {
        label: 'Logout',
        to: '/logout'
    }
])
const items = ref<NavigationMenuItem[]>([
    {
        label: 'About'
    },
    {
        label: 'Terms'
    },
    {
        label: 'Privacy'
    },
])

</script>