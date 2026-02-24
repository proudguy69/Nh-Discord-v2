<template>
    <UPageHero
    title="The biggest NH community"
    orientation="horizontal"
    description="Come join New Hampshire's biggest Discord server! check out our other related communities!"
    headline="New Update!"
    >
    <img src="/chat.png" alt="">
    </UPageHero>
    <UPageSection
    title="Our Servers"
    >
    <UPricingPlans :plans="servers"/>
    </UPageSection>
</template>

<script setup lang="ts">
import type { PricingPlanProps } from '@nuxt/ui'

const servers = ref<PricingPlanProps[]>([
    {
        title: '[18+] Live Free New Hampshire',
        description: 'The main general community for all New Hampshire related things',
        features: ['600+ Members', 'Active community'],
        button: {
            label: 'Join Now',
            color: 'neutral',
            to: 'https://discord.gg/PFM7gQJa2H'
        }
    },
    {
        title: '[13-17] Live Free Minors',
        description: 'Experimental NH discord for 13-17 users',
        features: [],
        button: {
            label: 'In development',
            disabled: true,
            color: 'neutral',
            variant: 'subtle'
        }
    },
    {
        title: '[18+] Live Free and Love',
        description: 'Experimental dating community free for all',
        features: [],
        button: {
            label: 'In development, waitlist soon!',
            color: 'neutral',
            disabled:true
        }
    },
])
    
</script>