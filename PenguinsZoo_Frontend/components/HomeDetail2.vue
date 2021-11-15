<template>
    <div>
        <div class="lg:mt-3 flex justify-center">
            <iframe
                class="lg:w-2/3 lg:h-96"
                src="https://www.youtube.com/embed/DqC3ieJJlFM?playlist=DqC3ieJJlFM&loop=1"
            >
            </iframe>
        </div>
        <div
            class="
                w-full
                bg-background
                mt-7
                py-3
                px-2
                lg:mt-8 lg:py-16 lg:px-8
                flex
                border-b
            "
        >
            <div class="w-96 mt-3 mr-3 lg:min-w-max lg:mr-12">
                <img src="../static/quotes.jpg" alt="quotes" />
            </div>
            <div>
                <p class="lg:text-2xl text-sm text-white lg:mt-20">
                    “Stop wildlife crime — it’s dead serious” is the tagline on
                    new World Wildlife Fund ads, which will run in print as well
                    as in spots like billboards and buses."
                </p>
            </div>
        </div>
        <div
            class="
                w-full
                bg-background
                py-6
                px-4
                lg:py-16 lg:px-8
                flex
                justify-center
            "
        >
            <div class="lg:w-1/6 h-44 lg:h-80 lg:pt-20">
                <div class="bg-gray-500 lg:h-60">
                    <div class="flex justify-center">
                        <h1 class="text-white lg:text-6xl lg:mt-2">2</h1>
                        <h1 class="text-white lg:text-3xl lg:mt-7 lg:ml-3">
                            Elephant
                        </h1>
                    </div>
                    <img class="lg:mt-3" src="../static/elephant.png" />
                </div>
            </div>
            <div class="lg:w-1/6 h-44 bg-red-800 lg:h-80 lg:pt-3">
                <div class="flex justify-center">
                    <h1 class="text-white lg:text-6xl">1</h1>
                    <h1 class="text-white lg:text-3xl lg:mt-5 lg:ml-3">
                        Tiger
                    </h1>
                </div>
                <img src="../static/tiger.png" />
            </div>
            <div class="lg:w-1/6 h-44 lg:h-80 lg:pt-32">
                <div class="bg-pangolin lg:h-48">
                    <div class="flex justify-center">
                        <h1 class="text-white lg:text-6xl lg:mt-5">3</h1>
                        <h1 class="text-white lg:text-3xl lg:mt-10 lg:ml-3">
                            Pangolin
                        </h1>
                    </div>
                    <img src="../static/tete.png" class="lg:ml-3 lg:h-36" />
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.bg-pangolin {
    background-color: #c37539;
}
</style>
