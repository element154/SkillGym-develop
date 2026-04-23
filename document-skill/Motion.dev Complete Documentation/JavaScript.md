# Get started with Motion â install, first animation | Motion

Source: https://motion.dev/docs/quick-start

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

# Get started with Motion

Motion is an animation library that's easy to start and fun to master.

Its unique hybrid engine combines the performance of the browser with the limitless potential of a JavaScript engine. This means you can animate anything, like:

- HTML/CSS

HTML/CSS

- SVG (like path drawing animations)

SVG (like path drawing animations)

- WebGL (3D graphics)

WebGL (3D graphics)

The best part? It's also tiny, with a mini HTML/SVG version of the animate() function that's just 2.3kb!

```
animate()
```

By the end of this quick guide, you'll have installed Motion and made your first animation.

## Install

You can install Motion in two ways:

- A package manager like npm or Yarn ( most popular)

A package manager like npm or Yarn ( most popular)

- HTML script tag

HTML script tag

```
script
```

### Package manager

Motion can be installed via the "motion" package.

```
"motion"
```

```
npm install motion
```

Then imported in your JavaScript:

```
import { animate , scroll } from "motion"
```

### script tag

```
script
```

It's possible to import Motion directly using a script tag. This is perfect if you're working with a basic HTML page, or using a no-code tool like Webflow.

```
script
```

Import using the modern import syntax:

```
import
```

```
< script type = "module" > import { animate , scroll } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm" </ script >
```

Or you can add Motion as a global variable using the legacy include:

```
Motion
```

```
< script src = "https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js" > </ script > < script > const { animate , scroll } = Motion </ script >
```

It's best practise to replace "latest" in these URLs with a specific version, like 11.11.13 . You can find the latest version in the site footer.

```
11.11.13
```

### Create an animation

The "Hello world!" of any animation library is a simple transform animation.

Let's start by importing the animate function .

```
animate
```

```
import { animate } from "motion"
```

animate can animate one or more elements. You can either use a CSS selector (like ".my-class" ) or provide the elements directly:

```
animate
```

```
".my-class"
```

```
// CSS selector animate ( ".box" , { rotate : 360 } ) // Elements const boxes = document . querySelectorAll ( ".box" ) animate ( boxes , { rotate : 360 } )
```

You can see here we're setting rotate to 360 . This will rotate the element 360 degrees:

```
rotate
```

```
360
```

## What can be animated?

Motion lets you animate anything:

- CSS properties (like opacity , transform and filter )

CSS properties (like opacity , transform and filter )

```
opacity
```

```
transform
```

```
filter
```

- SVG attributes and paths

SVG attributes and paths

- Independent transforms ( x , rotateY etc)

Independent transforms ( x , rotateY etc)

```
x
```

```
rotateY
```

- JavaScript objects (containing strings/colors/numbers)

JavaScript objects (containing strings/colors/numbers)

With Motion, you don't have to worry about achieving the best performance available. When a value can be hardware accelerated, like opacity , filter or transform , it will be.

```
opacity
```

```
filter
```

```
transform
```

animate isn't limited to HTML. It can animate single values or any kind of object. For example, the rotation of a Three.js object:

```
animate
```

```
animate ( cube . rotation , { y : rad ( 360 ) , z : rad ( 360 ) } , { duration : 10 , repeat : Infinity , ease : "linear" } )
```

## Customising animations

Motion comes with smart defaults, so your animations should look and feel great out of the box. But you can further tweak options like:

- Duration (how long the animation lasts)

Duration (how long the animation lasts)

- Delay (how long it waits before starting)

Delay (how long it waits before starting)

- Easing (how it speeds up and slows down)

Easing (how it speeds up and slows down)

- Repeat (how it repeats, how many times, etc)

Repeat (how it repeats, how many times, etc)

```
animate ( element , { scale : [ 0.4 , 1 ] } , { ease : "circInOut" , duration : 1.2 } ) ;
```

Motion also has amazing spring animations for natural, kinetic animations:

```
animate ( element , { rotate : 90 } , { type : "spring" , stiffness : 300 } ) ;
```

## Stagger animations

When animating multiple elements, it can feel more natural or lively to offset the animations of each. This is called staggering .

Motion provides a stagger function that can be used to dynamically set delay :

```
stagger
```

```
delay
```

```
import { animate , stagger } from "motion" animate ( "li" , { y : 0 , opacity : 1 } , { delay : stagger ( 0.1 ) } )
```

## Development tools

Motion Studio provides visual editing and AI tools to enhance your animation development workflow, like inline bezier editing, CSS spring generation and more.

### Install Motion Studio

One-click install for Cursor:

Add Extension

Add MCP

Motion Studio is also compatible with VS Code, Google Antigravity and more. See full installation guide .

### What's next?

You've just learned the basics of Motion and created a simple animation. But there's so much more to discover, like:

- Keyframes and sequences : Create more complex animations

Keyframes and sequences : Create more complex animations

- Controls : Pause, resume or change animations

Controls : Pause, resume or change animations

- Scroll-linked animations : Link values to scroll position

Scroll-linked animations : Link values to scroll position

- Scroll-triggered animations : Trigger animations when elements enter the viewport

Scroll-triggered animations : Trigger animations when elements enter the viewport

Or you can dive straight into our examples , which include copy & paste source code to add straight to your project.

Motion is an animation library that's easy to start and fun to master.

Its unique hybrid engine combines the performance of the browser with the limitless potential of a JavaScript engine. This means you can animate anything, like:

- HTML/CSS

HTML/CSS

- SVG (like path drawing animations)

SVG (like path drawing animations)

- WebGL (3D graphics)

WebGL (3D graphics)

The best part? It's also tiny, with a mini HTML/SVG version of the animate() function that's just 2.3kb!

```
animate()
```

By the end of this quick guide, you'll have installed Motion and made your first animation.

## Install

You can install Motion in two ways:

- A package manager like npm or Yarn ( most popular)

A package manager like npm or Yarn ( most popular)

- HTML script tag

HTML script tag

```
script
```

### Package manager

Motion can be installed via the "motion" package.

```
"motion"
```

```
npm install motion
```

Then imported in your JavaScript:

```
import { animate , scroll } from "motion"
```

### script tag

```
script
```

It's possible to import Motion directly using a script tag. This is perfect if you're working with a basic HTML page, or using a no-code tool like Webflow.

```
script
```

Import using the modern import syntax:

```
import
```

```
< script type = "module" > import { animate , scroll } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm" </ script >
```

Or you can add Motion as a global variable using the legacy include:

```
Motion
```

```
< script src = "https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js" > </ script > < script > const { animate , scroll } = Motion </ script >
```

It's best practise to replace "latest" in these URLs with a specific version, like 11.11.13 . You can find the latest version in the site footer.

```
11.11.13
```

### Create an animation

The "Hello world!" of any animation library is a simple transform animation.

Let's start by importing the animate function .

```
animate
```

```
import { animate } from "motion"
```

animate can animate one or more elements. You can either use a CSS selector (like ".my-class" ) or provide the elements directly:

```
animate
```

```
".my-class"
```

```
// CSS selector animate ( ".box" , { rotate : 360 } ) // Elements const boxes = document . querySelectorAll ( ".box" ) animate ( boxes , { rotate : 360 } )
```

You can see here we're setting rotate to 360 . This will rotate the element 360 degrees:

```
rotate
```

```
360
```

## What can be animated?

Motion lets you animate anything:

- CSS properties (like opacity , transform and filter )

CSS properties (like opacity , transform and filter )

```
opacity
```

```
transform
```

```
filter
```

- SVG attributes and paths

SVG attributes and paths

- Independent transforms ( x , rotateY etc)

Independent transforms ( x , rotateY etc)

```
x
```

```
rotateY
```

- JavaScript objects (containing strings/colors/numbers)

JavaScript objects (containing strings/colors/numbers)

With Motion, you don't have to worry about achieving the best performance available. When a value can be hardware accelerated, like opacity , filter or transform , it will be.

```
opacity
```

```
filter
```

```
transform
```

animate isn't limited to HTML. It can animate single values or any kind of object. For example, the rotation of a Three.js object:

```
animate
```

```
animate ( cube . rotation , { y : rad ( 360 ) , z : rad ( 360 ) } , { duration : 10 , repeat : Infinity , ease : "linear" } )
```

## Customising animations

Motion comes with smart defaults, so your animations should look and feel great out of the box. But you can further tweak options like:

- Duration (how long the animation lasts)

Duration (how long the animation lasts)

- Delay (how long it waits before starting)

Delay (how long it waits before starting)

- Easing (how it speeds up and slows down)

Easing (how it speeds up and slows down)

- Repeat (how it repeats, how many times, etc)

Repeat (how it repeats, how many times, etc)

```
animate ( element , { scale : [ 0.4 , 1 ] } , { ease : "circInOut" , duration : 1.2 } ) ;
```

Motion also has amazing spring animations for natural, kinetic animations:

```
animate ( element , { rotate : 90 } , { type : "spring" , stiffness : 300 } ) ;
```

## Stagger animations

When animating multiple elements, it can feel more natural or lively to offset the animations of each. This is called staggering .

Motion provides a stagger function that can be used to dynamically set delay :

```
stagger
```

```
delay
```

```
import { animate , stagger } from "motion" animate ( "li" , { y : 0 , opacity : 1 } , { delay : stagger ( 0.1 ) } )
```

## Development tools

Motion Studio provides visual editing and AI tools to enhance your animation development workflow, like inline bezier editing, CSS spring generation and more.

### Install Motion Studio

One-click install for Cursor:

Add Extension

Add MCP

Motion Studio is also compatible with VS Code, Google Antigravity and more. See full installation guide .

### What's next?

You've just learned the basics of Motion and created a simple animation. But there's so much more to discover, like:

- Keyframes and sequences : Create more complex animations

Keyframes and sequences : Create more complex animations

- Controls : Pause, resume or change animations

Controls : Pause, resume or change animations

- Scroll-linked animations : Link values to scroll position

Scroll-linked animations : Link values to scroll position

- Scroll-triggered animations : Trigger animations when elements enter the viewport

Scroll-triggered animations : Trigger animations when elements enter the viewport

Or you can dive straight into our examples , which include copy & paste source code to add straight to your project.

Motion is an animation library that's easy to start and fun to master.

Its unique hybrid engine combines the performance of the browser with the limitless potential of a JavaScript engine. This means you can animate anything, like:

- HTML/CSS

HTML/CSS

- SVG (like path drawing animations)

SVG (like path drawing animations)

- WebGL (3D graphics)

WebGL (3D graphics)

The best part? It's also tiny, with a mini HTML/SVG version of the animate() function that's just 2.3kb!

```
animate()
```

By the end of this quick guide, you'll have installed Motion and made your first animation.

## Install

You can install Motion in two ways:

- A package manager like npm or Yarn ( most popular)

A package manager like npm or Yarn ( most popular)

- HTML script tag

HTML script tag

```
script
```

### Package manager

Motion can be installed via the "motion" package.

```
"motion"
```

```
npm install motion
```

Then imported in your JavaScript:

```
import { animate , scroll } from "motion"
```

### script tag

```
script
```

It's possible to import Motion directly using a script tag. This is perfect if you're working with a basic HTML page, or using a no-code tool like Webflow.

```
script
```

Import using the modern import syntax:

```
import
```

```
< script type = "module" > import { animate , scroll } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm" </ script >
```

Or you can add Motion as a global variable using the legacy include:

```
Motion
```

```
< script src = "https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js" > </ script > < script > const { animate , scroll } = Motion </ script >
```

It's best practise to replace "latest" in these URLs with a specific version, like 11.11.13 . You can find the latest version in the site footer.

```
11.11.13
```

### Create an animation

The "Hello world!" of any animation library is a simple transform animation.

Let's start by importing the animate function .

```
animate
```

```
import { animate } from "motion"
```

animate can animate one or more elements. You can either use a CSS selector (like ".my-class" ) or provide the elements directly:

```
animate
```

```
".my-class"
```

```
// CSS selector animate ( ".box" , { rotate : 360 } ) // Elements const boxes = document . querySelectorAll ( ".box" ) animate ( boxes , { rotate : 360 } )
```

You can see here we're setting rotate to 360 . This will rotate the element 360 degrees:

```
rotate
```

```
360
```

## What can be animated?

Motion lets you animate anything:

- CSS properties (like opacity , transform and filter )

CSS properties (like opacity , transform and filter )

```
opacity
```

```
transform
```

```
filter
```

- SVG attributes and paths

SVG attributes and paths

- Independent transforms ( x , rotateY etc)

Independent transforms ( x , rotateY etc)

```
x
```

```
rotateY
```

- JavaScript objects (containing strings/colors/numbers)

JavaScript objects (containing strings/colors/numbers)

With Motion, you don't have to worry about achieving the best performance available. When a value can be hardware accelerated, like opacity , filter or transform , it will be.

```
opacity
```

```
filter
```

```
transform
```

animate isn't limited to HTML. It can animate single values or any kind of object. For example, the rotation of a Three.js object:

```
animate
```

```
animate ( cube . rotation , { y : rad ( 360 ) , z : rad ( 360 ) } , { duration : 10 , repeat : Infinity , ease : "linear" } )
```

## Customising animations

Motion comes with smart defaults, so your animations should look and feel great out of the box. But you can further tweak options like:

- Duration (how long the animation lasts)

Duration (how long the animation lasts)

- Delay (how long it waits before starting)

Delay (how long it waits before starting)

- Easing (how it speeds up and slows down)

Easing (how it speeds up and slows down)

- Repeat (how it repeats, how many times, etc)

Repeat (how it repeats, how many times, etc)

```
animate ( element , { scale : [ 0.4 , 1 ] } , { ease : "circInOut" , duration : 1.2 } ) ;
```

Motion also has amazing spring animations for natural, kinetic animations:

```
animate ( element , { rotate : 90 } , { type : "spring" , stiffness : 300 } ) ;
```

## Stagger animations

When animating multiple elements, it can feel more natural or lively to offset the animations of each. This is called staggering .

Motion provides a stagger function that can be used to dynamically set delay :

```
stagger
```

```
delay
```

```
import { animate , stagger } from "motion" animate ( "li" , { y : 0 , opacity : 1 } , { delay : stagger ( 0.1 ) } )
```

## Development tools

Motion Studio provides visual editing and AI tools to enhance your animation development workflow, like inline bezier editing, CSS spring generation and more.

### Install Motion Studio

One-click install for Cursor:

Add Extension

Add MCP

Motion Studio is also compatible with VS Code, Google Antigravity and more. See full installation guide .

### What's next?

You've just learned the basics of Motion and created a simple animation. But there's so much more to discover, like:

- Keyframes and sequences : Create more complex animations

Keyframes and sequences : Create more complex animations

- Controls : Pause, resume or change animations

Controls : Pause, resume or change animations

- Scroll-linked animations : Link values to scroll position

Scroll-linked animations : Link values to scroll position

- Scroll-triggered animations : Trigger animations when elements enter the viewport

Scroll-triggered animations : Trigger animations when elements enter the viewport

Or you can dive straight into our examples , which include copy & paste source code to add straight to your project.

Next

animate

AI-ready animations

Make your LLM an animation expert with 330+ pre-built examples available via MCP.
