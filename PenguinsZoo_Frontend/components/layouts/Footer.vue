<template>
    <div
        class="
            justify-center
            bottom-0
            w-full
            bg-primary
            text-white
            divide-y divide-gray-600
        "
    >
        <div class="flex justify-between px-48 py-3">
            <div>
                <h2 class="text-hover font-semibold">CONTACT US</h2>
                <div class="flex flex-col mt-3">
                    <NuxtLink to="/" class="flex text-sm hover:text-hover">
                        <Email class="mr-2"></Email>
                        <p>penguinszoo2021@gmail.com</p>
                    </NuxtLink>
                    <NuxtLink to="/" class="flex text-sm mt-1 hover:text-hover">
                        <Phone class="mr-2"></Phone>
                        <p>+84949534426</p>
                    </NuxtLink>
                </div>
            </div>
            <div>
                <h2 class="text-hover font-semibold">OUR COOPERATIONS</h2>
                <div class="flex flex-col mt-3">
                    <a
                        class="text-sm mt-1 hover:text-hover"
                        target="_blank"
                        href="https://vn.usembassy.gov/"
                    >
                        U.S. Consulate & Consulate Vietnam
                    </a>
                    <a
                        class="text-sm mt-1 hover:text-hover"
                        target="_blank"
                        href="https://wildaid.org/"
                    >
                        WILDAID
                    </a>
                    <a
                        class="text-sm mt-1 hover:text-hover"
                        target="_blank"
                        href="https://changevn.org/en/home/"
                    >
                        Changevn
                    </a>
                    <a
                        class="text-sm mt-1 hover:text-hover"
                        target="_blank"
                        href="https://daihoc.fpt.edu.vn/"
                    >
                        FPT University
                    </a>
                    <a
                        class="text-sm mt-1 hover:text-hover"
                        target="_blank"
                        href="https://www.vietseeds.org/"
                    >
                        Vietseeds
                    </a>
                </div>
            </div>
            <div>
                <h2 class="text-hover font-semibold">FOLLOW US</h2>
                <div class="flex mt-3">
                    <nuxt-link class="text-sm mr-3" to="/">
                        <Facebook class="contact-icon"></Facebook>
                    </nuxt-link>
                    <nuxt-link class="text-sm mr-3" to="/">
                        <Twitter class="contact-icon"></Twitter>
                    </nuxt-link>
                    <nuxt-link class="text-sm mr-3" to="/">
                        <Instagram class="contact-icon"></Instagram>
                    </nuxt-link>
                </div>
            </div>
        </div>

        <div class="my-3 py-3 flex justify-center">
            <div class="mr-4">
                <img
                    src="../../static/logo4.jpg"
                    width="50"
                    class="cursor-pointer"
                />
            </div>
            <div>
                <p class="text-gray-400 mt-3">
                    Copyright © 2021 Penguins Zoo Hackathon Vietnam
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import Email from '~/static/Email'
import Phone from '~/static/Phone'
import Facebook from '~/static/Facebook'
import Instagram from '~/static/Instagram'
import Twitter from '~/static/Twitter'
export default {
    name: 'footer',
    components: { Twitter, Instagram, Facebook, Phone, Email },
}
</script>

<style scoped>
.nuxt-logo {
    height: 35px;
}

.contact-icon:hover {
    fill: #f9cf1c;
}
</style>
