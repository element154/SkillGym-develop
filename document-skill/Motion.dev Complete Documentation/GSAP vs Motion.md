# GSAP vs Motion: A detailed comparison | Motion

Source: https://motion.dev/docs/gsap-vs-motion

## JS

## React

Vue

Studio

### Get started

### Examples

### Animation

- animate

animate

- scroll

scroll

- animateView

animateView

- animateLayout

animateLayout

- Easing

Easing

### Gestures & Events

- hover

hover

- inView

inView

- press

press

- resize

resize

### Utils

- delay

delay

- frame

frame

- mix

mix

- scrambleText Motion+

scrambleText

Motion+

- splitText

splitText

- spring

spring

- stagger

stagger

- transform

transform

- wrap

wrap

### Motion values

- motionValue

motionValue

- mapValue

mapValue

- transformValue

transformValue

- springValue

springValue

### Renderers

- attrEffect

attrEffect

- propEffect

propEffect

- styleEffect

styleEffect

- svgEffect

svgEffect

### Integrations

- CSS

CSS

- Squarespace

Squarespace

- Webflow

Webflow

- WordPress

WordPress

### Guides

- FAQs

FAQs

- GSAP vs Motion

GSAP vs Motion

- Improvements to Web Animations API

Improvements to Web Animations API

- GSAP migration

GSAP migration

- Performance

Performance

- Upgrade guide

Upgrade guide

JavaScript

Copy page

# GSAP vs Motion: Which should you use?

Ready to migrate? Check out our simple GSAP to Motion migration guide .

When deciding which JavaScript animation library to trust for your project, two libraries often get mentioned because of their feature set and popularity: Motion (formerly Framer Motion) and GSAP (formerly GreenSock).

Both can create stunning animations, but they have fundamental differences. This guide compares Motion and GSAP on adoption , licensing , performance , and features (complete with full comparison table), to help you decide which is right for your project.

## Adoption

Before delving into the libraries themselves, it's helpful to see what other developers are choosing. For modern applications, npm is a great measure of a library's adoption and momentum.

Here, the numbers are clear: Motion is growing exponentially, making it the most-used and fastest-growing animation library in the ecosystem. It even just passed 16 million downloads per month .

## Licensing

Motion is fully independent and MIT open source . It's financially supported by a mix of incredible industry-leading sponsors like Framer , Figma , Sanity , Tailwind CSS and LottieFiles , as well as sales from Motion+ .

GSAP, by contrast, is closed source and owned and funded by Webflow . While it can be used for free in many projects, its license contains a critical restriction: You're prohibited from using GSAP in any tool that competes with Webflow. Furthermore, its license states that Webflow can terminate it at its discretion .

With Motion, you have a guarantee of freedom . That MIT license is irrevocable. You will never be forced to remove and replace your animation library because of a business decision made by another company. This provides the stability and peace of mind that professional development teams require.

Motion's independence and self-sufficiency also means we work with a broad base of users and companies, creating a library that works for the whole web, rather than the interests of a single company.

## Performance

Performance is more than just smooth animations. It's about providing a flawless 120fps, faster start-up times, and minimal bundle sizes. This is where Motion's modern architecture provides an advantage.

### Hardware accelerated animations

You might already know that for best animation performance you should stick to animating opacity , transform , filter and clipPath , because these styles can be rendered entirely on the GPU .

```
opacity
```

```
transform
```

```
filter
```

```
clipPath
```

But when animating with Motion, these values can enjoy an extra performance boost using "hardware accelerated" animations. This means the animations themselves also run entirely the GPU - separate from the JavaScript running on your CPU.

This means if your website or app is performing heavy work, animations remain smooth .

To illustrate, in the following example the ball on the left is animated with Motion, and the ball on the right by a traditional animation library. Press the "Block JavaScript" button to block JS execution for two seconds:

In the majority of browsers, the left ball will continue animating at 60/120fps, even as the website becomes unresponsive. Traditional animation libraries like GSAP will pause and stutter where Motion remains perfectly smooth.

What's more, Motion can even perform hardware accelerated scroll animations . Because browsers render all scroll on the GPU, JS-based scroll animations are always slightly out-of-sync. Not so with Motion.

```
const animation = animate ( element , { opacity : [ 0 , 1 ] } ) scroll ( animation )
```

### Start-up time

Two animate any two values, they have to be mixable. Think, two numbers, or two colors. But what if we want to perform an animation where we don't even know the initial value? Or we do - but it's a value like height: auto , or a color defined in a CSS variable like var(âmy-color) ?

```
height: auto
```

```
var(âmy-color)
```

To make these values mixable, the library first needs to measure them. But measuring something that's just been rendered forces a layout or style calculation. These are slow.

To solve this, Motion introduced deferred keyframe resolution . This ensures we batch all measurements into a single operation, drastically reducing style and layout calculations.

In benchmarks, Motion is 2.5x faster than GSAP at animating from unknown values, and 6x faster at animating between different value types.

This is great for user experience, and also great for performance scores like Interaction to Next Paint (INP).

### Bundle size

Motion is built with a modern, modular architecture. If your bundler supports tree-shaking (like Vite, Rollup or Webpack), you only ever include the code you actually use. GSAP's older architecture, by contrast, means that importing any part of the library includes all of it.

This, combined with Motion's focus on leveraging native browser APIs, results in a significantly smaller footprint.

Library

Size

animate() (mini)

```
animate()
```

2.6kb

animate() (full)

```
animate()
```

18kb

GSAP

23kb

A smaller bundle means a faster site load and a better user experience , especially on mobile devices. With Motion, you can deliver stunning animations with a minimal performance cost.

## Features

Of course, performance means little if a library can't deliver the features you need. While there is plenty of overlap, both libraries have unique strengths.

### React & Vue APIs

Motion provides a first-class, declarative API that is a natural extension of React and Vue . Animations are defined directly in your components via props, keeping your code clean, readable and easy to maintain.

```
< motion . div animate = { { x : 100 } } />
```

GSAP, by contrast, uses an imperative model. While it has a useGSAP hook to help integrate into React's lifecycles, it still requires using refs. Mixing its imperative API into React's declarative components leads to more verbose and error-prone code.

```
useGSAP
```

```
const container = useRef ( ) useGSAP ( ( ) => { gsap . to ( ".box" , { x : 100 } ) } , { scope : container } ) return ( < div ref = { container } > < div className = "box" > </ div > </ div > ) ;
```

Furthermore, Motion for React and Vue features an industry-leading layout animation engine , which goes far beyond the FLIP animations in GSAP.

### Timelines & sequencing

GSAP is famous for its powerful timeline function, which uses an imperative, chain-based API to build complex animation sequences. It's mature, and an industry standard for good reason.

```
const tl = gsap . timeline ( ) tl . to ( "h1" , { opacity : 1 } ) tl . to ( "p" , { y : 0 } , "-=0.5" )
```

Motion provides a modern, declarative alternative. Instead of chain-based commands, animate() accepts a simple JavaScript array, making it easy to read, modify and dynamically generate animation sequences.

```
animate()
```

```
animate ( [ [ "h1" , { opacity : 1 } ] , [ "p" , { y : 0 } , { at : "-0.5" } ] ] )
```

This timeline can animate anything the animate() function can, mixing HTML elements, SVG elements, motion values , and even 3D objects from libraries like Three.js - all within the same sequence. As mentioned earlier, it's also 5kb lighter.

```
animate()
```

The benefit to GSAP's timeline API is that it's mutable . Once playback has begun, individual tracks can be added and removed to the overarching sequence, an ability that Motion doesn't yet offer.

### Full feature comparison table

This table compares Motion's mini and full-size animate functions functions with GSAP's gsap object.

```
animate
```

```
gsap
```

#### Key

- â  Supported

â  Supported

- â  Not supported

â  Not supported

- â©  Support relies on modern browser features

â©  Support relies on modern browser features

- ð§  In development

ð§  In development

- â  Partial support

â  Partial support

- âï¸  React/Vue only

âï¸  React/Vue only

animate mini

```
animate
```

animate

```
animate
```

GSAP

Core bundlesize (kb)

2.6

18

23.5

#### General

MIT license

â

â

â

Accelerated animations

â

â

â

React API

â

â (+15kb)

â

Vue API

â

â (+15kb)

â

#### Values

Individual transforms

â

â

â

Complex transform interpolation

â

â

â

Named colors

â

â

â  (20)

Color type conversion

â

â

â

To/from CSS variables

â

â

â

To/from CSS functions

â

â

â

Animate CSS variables

â â©

â

â

Simple keyframes

syntax

â

â

â

Wildcard keyframes

â

â

â

Relative values

â

â

â

#### Output

Element styles

â

â

â

Element attributes

â

â

â

Custom animations

â

â

â

#### Options

Duration

â

â

â

Direction

â

â

â

Repeat

â

â

â

Delay

â

â

â

End delay

â

â

â

Repeat delay

â

â

â

#### Stagger

Stagger

â (+0.1kb)

â (+0.1kb)

â

Min delay

â

â

â

Ease

â

â

â

Grid

â

â

â

#### Layout

Animate layout

â

â  (View)

â  (FLIP)

Transform-only

â

â âï¸

â

Scale correction

â

â âï¸

â

#### Timeline

Timeline

â (+0.6kb)

â

â

Selectors

â

â

â

Relative offsets

â

â

â

Absolute offsets

â

â

â

Start of previous offset

â

â

â

Percentage offsets

â

â

â

Label offsets

â

â

â

Segment stagger

â

â

â

Segment keyframes

â

â

â

#### Controls

Play

â

â

â

Pause

â

â

â

Finish

â

â

â

Reverse

â

â

â

Stop

â

â

â

Playback rate

â

â

â

#### Easing

Linear

â

â

â

Cubic bezier

â

â

â

Steps

â

â

â

Spring

â (+1kb)

â

â

Spring physics

â

â

â

Inertia

â

â

â

Custom easing functions

â â©

â

â

#### Events

Complete

â

â

â

Cancel

â

â

â

Start

â

â

â

Update

â

â

â

Repeat

â

â

â

#### Path

Motion path

â â©

â â©

â (+9.5kb)

Path morphing

â

â (+ Flubber )

â

Path drawing

â

â

â

#### Scroll

Scroll trigger

â (+0.5kb)

â (+0.5kb)

â (+12kb)

Scroll-linked animations

â (+2.5kb)

â (+2.5kb)

â (+12kb)

Hardware accelerated animations

â

â

â

#### Extra Features

AnimateNumber

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Cursor

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Split Text

â ( Motion+ )

â ( Motion+ )

â

Ticker

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Typewriter

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

View animations

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

## Conclusion

Both Motion and GSAP are powerful, production-ready libraries capable of creating stunning, award-winning animations. The best choice depends entirely on the priorities of your project and team.

### When to use Motion?

You should choose Motion if your priority is overall performance, a smaller bundle size, and a modern developer experience. Its use of native browser APIs, first-class React/Vue support, and truly open-source MIT license make it the definitive choice for building fast, modern web applications.

### When to use GSAP?

You might still prefer GSAP if your project requires intricate, timeline-sequenced animations on non-React sites . Its maturity and long history mean it is a reliable, if more traditional, choice.

When deciding which JavaScript animation library to trust for your project, two libraries often get mentioned because of their feature set and popularity: Motion (formerly Framer Motion) and GSAP (formerly GreenSock).

Both can create stunning animations, but they have fundamental differences. This guide compares Motion and GSAP on adoption , licensing , performance , and features (complete with full comparison table), to help you decide which is right for your project.

## Adoption

Before delving into the libraries themselves, it's helpful to see what other developers are choosing. For modern applications, npm is a great measure of a library's adoption and momentum.

Here, the numbers are clear: Motion is growing exponentially, making it the most-used and fastest-growing animation library in the ecosystem. It even just passed 16 million downloads per month .

## Licensing

Motion is fully independent and MIT open source . It's financially supported by a mix of incredible industry-leading sponsors like Framer , Figma , Sanity , Tailwind CSS and LottieFiles , as well as sales from Motion+ .

GSAP, by contrast, is closed source and owned and funded by Webflow . While it can be used for free in many projects, its license contains a critical restriction: You're prohibited from using GSAP in any tool that competes with Webflow. Furthermore, its license states that Webflow can terminate it at its discretion .

With Motion, you have a guarantee of freedom . That MIT license is irrevocable. You will never be forced to remove and replace your animation library because of a business decision made by another company. This provides the stability and peace of mind that professional development teams require.

Motion's independence and self-sufficiency also means we work with a broad base of users and companies, creating a library that works for the whole web, rather than the interests of a single company.

## Performance

Performance is more than just smooth animations. It's about providing a flawless 120fps, faster start-up times, and minimal bundle sizes. This is where Motion's modern architecture provides an advantage.

### Hardware accelerated animations

You might already know that for best animation performance you should stick to animating opacity , transform , filter and clipPath , because these styles can be rendered entirely on the GPU .

```
opacity
```

```
transform
```

```
filter
```

```
clipPath
```

But when animating with Motion, these values can enjoy an extra performance boost using "hardware accelerated" animations. This means the animations themselves also run entirely the GPU - separate from the JavaScript running on your CPU.

This means if your website or app is performing heavy work, animations remain smooth .

To illustrate, in the following example the ball on the left is animated with Motion, and the ball on the right by a traditional animation library. Press the "Block JavaScript" button to block JS execution for two seconds:

In the majority of browsers, the left ball will continue animating at 60/120fps, even as the website becomes unresponsive. Traditional animation libraries like GSAP will pause and stutter where Motion remains perfectly smooth.

What's more, Motion can even perform hardware accelerated scroll animations . Because browsers render all scroll on the GPU, JS-based scroll animations are always slightly out-of-sync. Not so with Motion.

```
const animation = animate ( element , { opacity : [ 0 , 1 ] } ) scroll ( animation )
```

### Start-up time

Two animate any two values, they have to be mixable. Think, two numbers, or two colors. But what if we want to perform an animation where we don't even know the initial value? Or we do - but it's a value like height: auto , or a color defined in a CSS variable like var(âmy-color) ?

```
height: auto
```

```
var(âmy-color)
```

To make these values mixable, the library first needs to measure them. But measuring something that's just been rendered forces a layout or style calculation. These are slow.

To solve this, Motion introduced deferred keyframe resolution . This ensures we batch all measurements into a single operation, drastically reducing style and layout calculations.

In benchmarks, Motion is 2.5x faster than GSAP at animating from unknown values, and 6x faster at animating between different value types.

This is great for user experience, and also great for performance scores like Interaction to Next Paint (INP).

### Bundle size

Motion is built with a modern, modular architecture. If your bundler supports tree-shaking (like Vite, Rollup or Webpack), you only ever include the code you actually use. GSAP's older architecture, by contrast, means that importing any part of the library includes all of it.

This, combined with Motion's focus on leveraging native browser APIs, results in a significantly smaller footprint.

Library

Size

animate() (mini)

```
animate()
```

2.6kb

animate() (full)

```
animate()
```

18kb

GSAP

23kb

A smaller bundle means a faster site load and a better user experience , especially on mobile devices. With Motion, you can deliver stunning animations with a minimal performance cost.

## Features

Of course, performance means little if a library can't deliver the features you need. While there is plenty of overlap, both libraries have unique strengths.

### React & Vue APIs

Motion provides a first-class, declarative API that is a natural extension of React and Vue . Animations are defined directly in your components via props, keeping your code clean, readable and easy to maintain.

```
< motion . div animate = { { x : 100 } } />
```

GSAP, by contrast, uses an imperative model. While it has a useGSAP hook to help integrate into React's lifecycles, it still requires using refs. Mixing its imperative API into React's declarative components leads to more verbose and error-prone code.

```
useGSAP
```

```
const container = useRef ( ) useGSAP ( ( ) => { gsap . to ( ".box" , { x : 100 } ) } , { scope : container } ) return ( < div ref = { container } > < div className = "box" > </ div > </ div > ) ;
```

Furthermore, Motion for React and Vue features an industry-leading layout animation engine , which goes far beyond the FLIP animations in GSAP.

### Timelines & sequencing

GSAP is famous for its powerful timeline function, which uses an imperative, chain-based API to build complex animation sequences. It's mature, and an industry standard for good reason.

```
const tl = gsap . timeline ( ) tl . to ( "h1" , { opacity : 1 } ) tl . to ( "p" , { y : 0 } , "-=0.5" )
```

Motion provides a modern, declarative alternative. Instead of chain-based commands, animate() accepts a simple JavaScript array, making it easy to read, modify and dynamically generate animation sequences.

```
animate()
```

```
animate ( [ [ "h1" , { opacity : 1 } ] , [ "p" , { y : 0 } , { at : "-0.5" } ] ] )
```

This timeline can animate anything the animate() function can, mixing HTML elements, SVG elements, motion values , and even 3D objects from libraries like Three.js - all within the same sequence. As mentioned earlier, it's also 5kb lighter.

```
animate()
```

The benefit to GSAP's timeline API is that it's mutable . Once playback has begun, individual tracks can be added and removed to the overarching sequence, an ability that Motion doesn't yet offer.

### Full feature comparison table

This table compares Motion's mini and full-size animate functions functions with GSAP's gsap object.

```
animate
```

```
gsap
```

#### Key

- â  Supported

â  Supported

- â  Not supported

â  Not supported

- â©  Support relies on modern browser features

â©  Support relies on modern browser features

- ð§  In development

ð§  In development

- â  Partial support

â  Partial support

- âï¸  React/Vue only

âï¸  React/Vue only

animate mini

```
animate
```

animate

```
animate
```

GSAP

Core bundlesize (kb)

2.6

18

23.5

#### General

MIT license

â

â

â

Accelerated animations

â

â

â

React API

â

â (+15kb)

â

Vue API

â

â (+15kb)

â

#### Values

Individual transforms

â

â

â

Complex transform interpolation

â

â

â

Named colors

â

â

â  (20)

Color type conversion

â

â

â

To/from CSS variables

â

â

â

To/from CSS functions

â

â

â

Animate CSS variables

â â©

â

â

Simple keyframes

syntax

â

â

â

Wildcard keyframes

â

â

â

Relative values

â

â

â

#### Output

Element styles

â

â

â

Element attributes

â

â

â

Custom animations

â

â

â

#### Options

Duration

â

â

â

Direction

â

â

â

Repeat

â

â

â

Delay

â

â

â

End delay

â

â

â

Repeat delay

â

â

â

#### Stagger

Stagger

â (+0.1kb)

â (+0.1kb)

â

Min delay

â

â

â

Ease

â

â

â

Grid

â

â

â

#### Layout

Animate layout

â

â  (View)

â  (FLIP)

Transform-only

â

â âï¸

â

Scale correction

â

â âï¸

â

#### Timeline

Timeline

â (+0.6kb)

â

â

Selectors

â

â

â

Relative offsets

â

â

â

Absolute offsets

â

â

â

Start of previous offset

â

â

â

Percentage offsets

â

â

â

Label offsets

â

â

â

Segment stagger

â

â

â

Segment keyframes

â

â

â

#### Controls

Play

â

â

â

Pause

â

â

â

Finish

â

â

â

Reverse

â

â

â

Stop

â

â

â

Playback rate

â

â

â

#### Easing

Linear

â

â

â

Cubic bezier

â

â

â

Steps

â

â

â

Spring

â (+1kb)

â

â

Spring physics

â

â

â

Inertia

â

â

â

Custom easing functions

â â©

â

â

#### Events

Complete

â

â

â

Cancel

â

â

â

Start

â

â

â

Update

â

â

â

Repeat

â

â

â

#### Path

Motion path

â â©

â â©

â (+9.5kb)

Path morphing

â

â (+ Flubber )

â

Path drawing

â

â

â

#### Scroll

Scroll trigger

â (+0.5kb)

â (+0.5kb)

â (+12kb)

Scroll-linked animations

â (+2.5kb)

â (+2.5kb)

â (+12kb)

Hardware accelerated animations

â

â

â

#### Extra Features

AnimateNumber

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Cursor

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Split Text

â ( Motion+ )

â ( Motion+ )

â

Ticker

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Typewriter

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

View animations

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

## Conclusion

Both Motion and GSAP are powerful, production-ready libraries capable of creating stunning, award-winning animations. The best choice depends entirely on the priorities of your project and team.

### When to use Motion?

You should choose Motion if your priority is overall performance, a smaller bundle size, and a modern developer experience. Its use of native browser APIs, first-class React/Vue support, and truly open-source MIT license make it the definitive choice for building fast, modern web applications.

### When to use GSAP?

You might still prefer GSAP if your project requires intricate, timeline-sequenced animations on non-React sites . Its maturity and long history mean it is a reliable, if more traditional, choice.

When deciding which JavaScript animation library to trust for your project, two libraries often get mentioned because of their feature set and popularity: Motion (formerly Framer Motion) and GSAP (formerly GreenSock).

Both can create stunning animations, but they have fundamental differences. This guide compares Motion and GSAP on adoption , licensing , performance , and features (complete with full comparison table), to help you decide which is right for your project.

## Adoption

Before delving into the libraries themselves, it's helpful to see what other developers are choosing. For modern applications, npm is a great measure of a library's adoption and momentum.

Here, the numbers are clear: Motion is growing exponentially, making it the most-used and fastest-growing animation library in the ecosystem. It even just passed 16 million downloads per month .

## Licensing

Motion is fully independent and MIT open source . It's financially supported by a mix of incredible industry-leading sponsors like Framer , Figma , Sanity , Tailwind CSS and LottieFiles , as well as sales from Motion+ .

GSAP, by contrast, is closed source and owned and funded by Webflow . While it can be used for free in many projects, its license contains a critical restriction: You're prohibited from using GSAP in any tool that competes with Webflow. Furthermore, its license states that Webflow can terminate it at its discretion .

With Motion, you have a guarantee of freedom . That MIT license is irrevocable. You will never be forced to remove and replace your animation library because of a business decision made by another company. This provides the stability and peace of mind that professional development teams require.

Motion's independence and self-sufficiency also means we work with a broad base of users and companies, creating a library that works for the whole web, rather than the interests of a single company.

## Performance

Performance is more than just smooth animations. It's about providing a flawless 120fps, faster start-up times, and minimal bundle sizes. This is where Motion's modern architecture provides an advantage.

### Hardware accelerated animations

You might already know that for best animation performance you should stick to animating opacity , transform , filter and clipPath , because these styles can be rendered entirely on the GPU .

```
opacity
```

```
transform
```

```
filter
```

```
clipPath
```

But when animating with Motion, these values can enjoy an extra performance boost using "hardware accelerated" animations. This means the animations themselves also run entirely the GPU - separate from the JavaScript running on your CPU.

This means if your website or app is performing heavy work, animations remain smooth .

To illustrate, in the following example the ball on the left is animated with Motion, and the ball on the right by a traditional animation library. Press the "Block JavaScript" button to block JS execution for two seconds:

In the majority of browsers, the left ball will continue animating at 60/120fps, even as the website becomes unresponsive. Traditional animation libraries like GSAP will pause and stutter where Motion remains perfectly smooth.

What's more, Motion can even perform hardware accelerated scroll animations . Because browsers render all scroll on the GPU, JS-based scroll animations are always slightly out-of-sync. Not so with Motion.

```
const animation = animate ( element , { opacity : [ 0 , 1 ] } ) scroll ( animation )
```

### Start-up time

Two animate any two values, they have to be mixable. Think, two numbers, or two colors. But what if we want to perform an animation where we don't even know the initial value? Or we do - but it's a value like height: auto , or a color defined in a CSS variable like var(âmy-color) ?

```
height: auto
```

```
var(âmy-color)
```

To make these values mixable, the library first needs to measure them. But measuring something that's just been rendered forces a layout or style calculation. These are slow.

To solve this, Motion introduced deferred keyframe resolution . This ensures we batch all measurements into a single operation, drastically reducing style and layout calculations.

In benchmarks, Motion is 2.5x faster than GSAP at animating from unknown values, and 6x faster at animating between different value types.

This is great for user experience, and also great for performance scores like Interaction to Next Paint (INP).

### Bundle size

Motion is built with a modern, modular architecture. If your bundler supports tree-shaking (like Vite, Rollup or Webpack), you only ever include the code you actually use. GSAP's older architecture, by contrast, means that importing any part of the library includes all of it.

This, combined with Motion's focus on leveraging native browser APIs, results in a significantly smaller footprint.

Library

Size

animate() (mini)

```
animate()
```

2.6kb

animate() (full)

```
animate()
```

18kb

GSAP

23kb

A smaller bundle means a faster site load and a better user experience , especially on mobile devices. With Motion, you can deliver stunning animations with a minimal performance cost.

## Features

Of course, performance means little if a library can't deliver the features you need. While there is plenty of overlap, both libraries have unique strengths.

### React & Vue APIs

Motion provides a first-class, declarative API that is a natural extension of React and Vue . Animations are defined directly in your components via props, keeping your code clean, readable and easy to maintain.

```
< motion . div animate = { { x : 100 } } />
```

GSAP, by contrast, uses an imperative model. While it has a useGSAP hook to help integrate into React's lifecycles, it still requires using refs. Mixing its imperative API into React's declarative components leads to more verbose and error-prone code.

```
useGSAP
```

```
const container = useRef ( ) useGSAP ( ( ) => { gsap . to ( ".box" , { x : 100 } ) } , { scope : container } ) return ( < div ref = { container } > < div className = "box" > </ div > </ div > ) ;
```

Furthermore, Motion for React and Vue features an industry-leading layout animation engine , which goes far beyond the FLIP animations in GSAP.

### Timelines & sequencing

GSAP is famous for its powerful timeline function, which uses an imperative, chain-based API to build complex animation sequences. It's mature, and an industry standard for good reason.

```
const tl = gsap . timeline ( ) tl . to ( "h1" , { opacity : 1 } ) tl . to ( "p" , { y : 0 } , "-=0.5" )
```

Motion provides a modern, declarative alternative. Instead of chain-based commands, animate() accepts a simple JavaScript array, making it easy to read, modify and dynamically generate animation sequences.

```
animate()
```

```
animate ( [ [ "h1" , { opacity : 1 } ] , [ "p" , { y : 0 } , { at : "-0.5" } ] ] )
```

This timeline can animate anything the animate() function can, mixing HTML elements, SVG elements, motion values , and even 3D objects from libraries like Three.js - all within the same sequence. As mentioned earlier, it's also 5kb lighter.

```
animate()
```

The benefit to GSAP's timeline API is that it's mutable . Once playback has begun, individual tracks can be added and removed to the overarching sequence, an ability that Motion doesn't yet offer.

### Full feature comparison table

This table compares Motion's mini and full-size animate functions functions with GSAP's gsap object.

```
animate
```

```
gsap
```

#### Key

- â  Supported

â  Supported

- â  Not supported

â  Not supported

- â©  Support relies on modern browser features

â©  Support relies on modern browser features

- ð§  In development

ð§  In development

- â  Partial support

â  Partial support

- âï¸  React/Vue only

âï¸  React/Vue only

animate mini

```
animate
```

animate

```
animate
```

GSAP

Core bundlesize (kb)

2.6

18

23.5

#### General

MIT license

â

â

â

Accelerated animations

â

â

â

React API

â

â (+15kb)

â

Vue API

â

â (+15kb)

â

#### Values

Individual transforms

â

â

â

Complex transform interpolation

â

â

â

Named colors

â

â

â  (20)

Color type conversion

â

â

â

To/from CSS variables

â

â

â

To/from CSS functions

â

â

â

Animate CSS variables

â â©

â

â

Simple keyframes

syntax

â

â

â

Wildcard keyframes

â

â

â

Relative values

â

â

â

#### Output

Element styles

â

â

â

Element attributes

â

â

â

Custom animations

â

â

â

#### Options

Duration

â

â

â

Direction

â

â

â

Repeat

â

â

â

Delay

â

â

â

End delay

â

â

â

Repeat delay

â

â

â

#### Stagger

Stagger

â (+0.1kb)

â (+0.1kb)

â

Min delay

â

â

â

Ease

â

â

â

Grid

â

â

â

#### Layout

Animate layout

â

â  (View)

â  (FLIP)

Transform-only

â

â âï¸

â

Scale correction

â

â âï¸

â

#### Timeline

Timeline

â (+0.6kb)

â

â

Selectors

â

â

â

Relative offsets

â

â

â

Absolute offsets

â

â

â

Start of previous offset

â

â

â

Percentage offsets

â

â

â

Label offsets

â

â

â

Segment stagger

â

â

â

Segment keyframes

â

â

â

#### Controls

Play

â

â

â

Pause

â

â

â

Finish

â

â

â

Reverse

â

â

â

Stop

â

â

â

Playback rate

â

â

â

#### Easing

Linear

â

â

â

Cubic bezier

â

â

â

Steps

â

â

â

Spring

â (+1kb)

â

â

Spring physics

â

â

â

Inertia

â

â

â

Custom easing functions

â â©

â

â

#### Events

Complete

â

â

â

Cancel

â

â

â

Start

â

â

â

Update

â

â

â

Repeat

â

â

â

#### Path

Motion path

â â©

â â©

â (+9.5kb)

Path morphing

â

â (+ Flubber )

â

Path drawing

â

â

â

#### Scroll

Scroll trigger

â (+0.5kb)

â (+0.5kb)

â (+12kb)

Scroll-linked animations

â (+2.5kb)

â (+2.5kb)

â (+12kb)

Hardware accelerated animations

â

â

â

#### Extra Features

AnimateNumber

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Cursor

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Split Text

â ( Motion+ )

â ( Motion+ )

â

Ticker

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

Typewriter

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

View animations

âï¸ ( Motion+ )

âï¸ ( Motion+ )

â

## Conclusion

Both Motion and GSAP are powerful, production-ready libraries capable of creating stunning, award-winning animations. The best choice depends entirely on the priorities of your project and team.

### When to use Motion?

You should choose Motion if your priority is overall performance, a smaller bundle size, and a modern developer experience. Its use of native browser APIs, first-class React/Vue support, and truly open-source MIT license make it the definitive choice for building fast, modern web applications.

### When to use GSAP?

You might still prefer GSAP if your project requires intricate, timeline-sequenced animations on non-React sites . Its maturity and long history mean it is a reliable, if more traditional, choice.

Previous

FAQs

Next

Improvements to Web Animations API

Motion+

## Level up your animations with Motion+

Unlock the full vault of 330+ Motion examples, 100+ tutorials, premium APIs, private Discord and GitHub, and powerful Motion Studio animation editing tools for your IDE.

Get Motion+

Get Motion+

One-time payment, lifetime updates.

AI-ready animations

Make your LLM an animation expert with 330+ pre-built examples available via MCP.
