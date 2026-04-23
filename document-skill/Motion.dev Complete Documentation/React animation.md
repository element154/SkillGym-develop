# React Animation | Keyframes, Transitions & Gestures | Motion

Source: https://motion.dev/docs/react-animation

## JS

## React

Vue

Studio

### Get started

### Examples

### Courses

### Animation

- Overview

Overview

- Layout

Layout

- Scroll

Scroll

- SVG

SVG

- Transitions

Transitions

### Gestures

- Overview

Overview

- Hover

Hover

- Drag

Drag

### Components

- Motion component

Motion component

- AnimateActivity

AnimateActivity

- AnimatePresence

AnimatePresence

- AnimateView

AnimateView

- LayoutGroup

LayoutGroup

- LazyMotion

LazyMotion

- MotionConfig

MotionConfig

- Reorder

Reorder

### Premium APIs

- AnimateNumber

AnimateNumber

- Carousel

Carousel

- Cursor

Cursor

- ScrambleText

ScrambleText

- Ticker

Ticker

- Typewriter

Typewriter

### Motion values

- Overview

Overview

- useMotionTemplate

useMotionTemplate

- useMotionValueEvent

useMotionValueEvent

- useScroll

useScroll

- useSpring

useSpring

- useTime

useTime

- useTransform

useTransform

- useVelocity

useVelocity

### Hooks

- useAnimate

useAnimate

- useAnimationFrame

useAnimationFrame

- useDragControls

useDragControls

- useInView

useInView

- usePageInView

usePageInView

- useReducedMotion

useReducedMotion

### Integrations

- Framer

Framer

- Figma

Figma

- Tailwind CSS

Tailwind CSS

- Base UI

Base UI

- Radix

Radix

### Guides

- Installation

Installation

- Upgrade guide

Upgrade guide

- Accessibility

Accessibility

- Reduce bundle size

Reduce bundle size

React

Copy page

# React animation

New to Motion? Start with the Motion for React quickstart guide

Motion for React is a simple yet powerful animation library. Whether you're building hover effects, scroll-triggered animations, or complex animation sequences, this guide will provide an overview of all the ways you can animate in React with Motion.

## What you'll learn

- How to create your first animation with the <motion.div /> component.

How to create your first animation with the <motion.div /> component.

```
<motion.div />
```

- Which values and elements you can animate.

Which values and elements you can animate.

- How to customise your animations with transition options.

How to customise your animations with transition options.

- How to animate elements as they enter and exit the DOM.

How to animate elements as they enter and exit the DOM.

- How to orchestrate animations with variants.

How to orchestrate animations with variants.

If you haven't installed Motion already, hop over to the quick start guide for full instructions .

## Animate with <motion />

```
<motion />
```

Most animations in Motion are created with the <motion /> component . Import it from "motion/react" :

```
<motion />
```

```
"motion/react"
```

```
import { motion } from "motion/react"
```

Every HTML & SVG element can be defined with a motion component:

```
motion
```

```
< motion . div />
```

```
< motion . a href = "#" />
```

```
< motion . circle cx = { 0 } />
```

These work identically to their HTML/SVG counterparts - same props, same behaviour - but with additional animation props like animate , whileHover , and exit .

```
animate
```

```
whileHover
```

```
exit
```

The most common animation prop is animate . When values passed to animate change, the element will automatically animate to that value.

```
animate
```

```
animate
```

```
< motion . div animate = { { opacity : 1 } } />
```

### Enter animations

We can set initial values for an element with the initial prop. So an element defined like this will fade in when it enters the DOM:

```
initial
```

```
< motion . article initial = { { opacity : 0 } } animate = { { opacity : 1 } } />
```

## Animatable values

Motion can animate any CSS value , like opacity , filter etc.

```
opacity
```

```
filter
```

```
< motion . section initial = { { filter : "blur(10px)" } } animate = { { filter : "none" } } />
```

It can even animate values that aren't normally animatable by browsers, like background-image or mask-image :

```
background-image
```

```
mask-image
```

```
< motion . nav initial = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,0) 100%)" } } animate = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,1) 100%)" } } />
```

### Transforms

Unlike CSS, Motion can animate every transform axis independently.

```
< motion . div animate = { { x : 100 } } />
```

It supports the following special transform values:

- Translate: x , y , z

Translate: x , y , z

```
x
```

```
y
```

```
z
```

- Scale: scale , scaleX , scaleY

Scale: scale , scaleX , scaleY

```
scale
```

```
scaleX
```

```
scaleY
```

- Rotate: rotate , rotateX , rotateY , rotateZ

Rotate: rotate , rotateX , rotateY , rotateZ

```
rotate
```

```
rotateX
```

```
rotateY
```

```
rotateZ
```

- Skew: skewX , skewY

Skew: skewX , skewY

```
skewX
```

```
skewY
```

- Perspective: transformPerspective

Perspective: transformPerspective

```
transformPerspective
```

motion components also have enhanced style props, allowing you to use these shorthands statically:

```
motion
```

```
style
```

```
< motion . section style = { { x : - 20 } } />
```

Animating transforms independently provides great flexibility, especially when animating different transforms with gestures:

```
< motion . button initial = { { y : 10 } } animate = { { y : 0 } } whileHover = { { scale : 1.1 } } whileTap = { { scale : 0.9 } } />
```

Independent transforms already perform great, but Motion uniquely offers hardware acceleration when setting transform directly.

```
transform
```

```
< motion . li initial = { { transform : "translateX(-100px)" } } animate = { { transform : "translateX(0px)" } } transition = { { type : "spring" } } />
```

For SVG components, x and y attributes can be set using attrX and attrY . Learn more about SVG animations in React .

```
x
```

```
y
```

```
attrX
```

```
attrY
```

### Supported value types

Motion can animate any of the following value types:

- Numbers: 0 , 100 etc.

Numbers: 0 , 100 etc.

```
0
```

```
100
```

- Strings containing numbers: "0vh" , "10px" etc.

Strings containing numbers: "0vh" , "10px" etc.

```
"0vh"
```

```
"10px"
```

- Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

```
rgba
```

```
hsla
```

```
oklch
```

```
oklab
```

```
color-mix
```

- Complex strings containing multiple numbers and/or colors (like box-shadow ).

Complex strings containing multiple numbers and/or colors (like box-shadow ).

```
box-shadow
```

- display: "none"/"block" and visibility: "hidden"/"visible" .

display: "none"/"block" and visibility: "hidden"/"visible" .

```
display: "none"/"block"
```

```
visibility: "hidden"/"visible"
```

### Value type conversion

In general, values can only be animated between two of the same type (i.e "0px" to "100px" ).

```
"0px"
```

```
"100px"
```

Colors can be freely animated between hex, RGBA and HSLA types.

Additionally, x , y , width , height , top , left , right and bottom can animate between different value types.

```
x
```

```
y
```

```
width
```

```
height
```

```
top
```

```
left
```

```
right
```

```
bottom
```

```
< motion . div initial = { { x : "100%" } } animate = { { x : "calc(100vw - 50%)" } } />
```

It's also possible to animate width and height in to/out of "auto" .

```
width
```

```
height
```

```
"auto"
```

```
< motion . div initial = { { height : 0 } } animate = { { height : "auto" } } />
```

If animating height: auto while also animating display in to/out of "none" , replace this with visibility "hidden" as elements with display: none can't be measured.

```
height: auto
```

```
display
```

```
"none"
```

```
visibility
```

```
"hidden"
```

```
display: none
```

### Transform origin

transform-origin has three shortcut values that can be set and animated individually:

```
transform-origin
```

- originX

originX

```
originX
```

- originY

originY

```
originY
```

- originZ

originZ

```
originZ
```

If set as numbers, originX and Y default to a progress value between 0 and 1 . originZ defaults to pixels.

```
originX
```

```
Y
```

```
0
```

```
1
```

```
originZ
```

```
< motion . div style = { { originX : 0.5 } } />
```

### CSS variables

Motion for React can animate CSS variables, and also use CSS variable definitions as animation targets.

#### Animating CSS variables

Sometimes it's convenient to be able to animate a CSS variable to animate many children:

```
< motion . ul initial = { { '--rotate' : '0deg' } } animate = { { '--rotate' : '360deg' } } transition = { { duration : 2 , repeat : Infinity } } > < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> </ motion . ul >
```

Animating the value of a CSS variable always triggers paint , therefore it can be more performant to use MotionValue s to setup this kind of animation. Learn more about web animation performance .

```
MotionValue
```

#### Check your MotionScore

Enter a URL to audit your site's animation performance.

Check

### CSS variables as animation targets

HTML motion components accept animation targets with CSS variables:

```
motion
```

```
< motion . li animate = { { backgroundColor : "var(--action-bg)" } } />
```

## Transitions

By default, Motion will create appropriate transitions for snappy animations based on the type of value being animated.

For instance, physical properties like x or scale are animated with spring physics, whereas values like opacity or color are animated with duration-based easing curves.

```
x
```

```
scale
```

```
opacity
```

```
color
```

However, you can define your own animations via the transition prop .

```
transition
```

```
< motion . div animate = { { x : 100 } } transition = { { ease : "easeOut" , duration : 2 } } />
```

A default transition can be set for many components with the MotionConfig component :

```
transition
```

```
MotionConfig
```

```
< MotionConfig transition = { { duration : 0.3 } } > < motion . div animate = { { opacity : 1 } } />
```

Or you can set a specific transition on any animation prop:

```
transition
```

```
< motion . div animate = { { opacity : 1 } } whileHover = { { opacity : 0.7 , // Specific transitions override default transitions transition : { duration : 0.3 } } } transition = { { duration : 0.5 } } />
```

## Enter animations

When a motion component is first created, it'll automatically animate to the values in animate if they're different from those initially rendered, which you can either do via CSS or via the initial prop.

```
motion
```

```
animate
```

```
initial
```

```
< motion . li initial = { { opacity : 0 , scale : 0 } } animate = { { opacity : 1 , scale : 1 } } />
```

You can also disable the enter animation entirely by setting initial={false} . This will make the element render with the values defined in animate .

```
initial={false}
```

```
animate
```

```
< motion . div initial = { false } animate = { { y : 100 } } />
```

## Exit animations

Motion for React can animate elements as they're removed from the DOM.

In React, when a component is removed, it's usually removed instantly. Motion provides the AnimatePresence component which keeps elements in the DOM while they perform an animation defined with the exit prop.

```
AnimatePresence
```

```
exit
```

```
< AnimatePresence > { isVisible && ( < motion . div key = "modal" initial = { { opacity : 0 } } animate = { { opacity : 1 } } exit = { { opacity : 0 } } /> ) } </ AnimatePresence >
```

## Keyframes

So far, we've set animation props like animate and exit to single values, like opacity: 0 .

```
animate
```

```
exit
```

```
opacity: 0
```

This is great when we want to animate from the current value to a new value. But sometimes we want to animate through a series of values . In animation terms, these are called keyframes .

All animation props can accept keyframe arrays:

```
< motion . div animate = { { x : [ 0 , 100 , 0 ] } } />
```

When we animate to an array of values, the element will animate through each of these values in sequence.

In the previous example, we explicitly set the initial value as 0 . But we can also say "use the current value" by setting the first value to null .

```
0
```

```
null
```

```
< motion . div animate = { { x : [ null , 100 , 0 ] } } />
```

This way, if a keyframe animation is interrupting another animation, the transition will feel more natural.

### Wildcard keyframes

This null keyframe is called a wildcard keyframe . A wildcard keyframe simply takes the value before it (or the current value, if this is the first keyframe in the array).

```
null
```

Wildcard keyframes can be useful for holding a value mid-animation without having to repeat values.

```
< motion . div animate = { { x : [ 0 , 100 , null , 0 ] } } // same as x: [0, 100, 100, 0] but easier to maintain />
```

### Keyframe timing

By default, each keyframe is spaced evenly throughout the animation. You can override this by setting the times option via transition .

```
times
```

```
transition
```

times is an array of progress values between 0 and 1 , defining where in the animation each keyframe should be positioned.

```
times
```

```
0
```

```
1
```

```
< motion . circle cx = { 500 } animate = { { cx : [ null , 100 , 200 ] , transition : { duration : 3 , times : [ 0 , 0.2 , 1 ] } } } />
```

0 is the start of the animation, and 1 is the end of the animation. Therefore, 0.2 places this keyframe somewhere towards the start of the animation.

```
0
```

```
1
```

```
0.2
```

#### Stay in the loop

Sign up for the Motion newsletter.

Subscribe

## Gesture animations

Motion for React has animation props that can define how an element animates when it recognises a gesture .

Supported gestures are:

- whileHover

whileHover

```
whileHover
```

- whileTap

whileTap

```
whileTap
```

- whileFocus

whileFocus

```
whileFocus
```

- whileDrag

whileDrag

```
whileDrag
```

- whileInView

whileInView

```
whileInView
```

When a gesture starts, it animates to the values defined in while- , and then when the gesture ends it animates back to the values in initial or animate .

```
while-
```

```
initial
```

```
animate
```

```
< motion . button initial = { { opacity : 0 } } whileHover = { { backgroundColor : "rgba(220, 220, 220, 1)" } } whileTap = { { backgroundColor : "rgba(255, 255, 255, 1)" } } whileInView = { { opacity : 1 } } />
```

The custom Cursor component available in Motion+ takes this a step further with magnetic and target-morphing effects as a user hovers clickable targets (like buttons and links):

```
< Cursor magnetic />
```

## Variants

The animate prop works well for single elements, but real interfaces often need coordinated animations across parent and child components. Variants solve this by defining named animation states that propagate through the component tree.

```
animate
```

Variants are a set of named targets. These names can be anything.

```
const variants = { visible : { opacity : 1 } , hidden : { opacity : 0 } , }
```

Variants are passed to motion components via the variants prop:

```
motion
```

```
variants
```

```
< motion . div variants = { variants } />
```

These variants can now be referred to by a label, wherever you can define an animation target:

```
< motion . div variants = { variants } initial = "hidden" whileInView = "visible" exit = "hidden" />
```

You can also define multiple variants via an array:

```
animate = { [ "visible" , "danger" ] }
```

### Propagation

Variants are useful for reusing and combining animation targets. But it becomes powerful for orchestrating animations throughout trees.

Variants will flow down through motion components. So in this example when the ul enters the viewport, all of its children with a "visible" variant will also animate in:

```
motion
```

```
ul
```

```
const list = { visible : { opacity : 1 } , hidden : { opacity : 0 } , } const item = { visible : { opacity : 1 , x : 0 } , hidden : { opacity : 0 , x : - 100 } , } return ( < motion . ul initial = "hidden" whileInView = "visible" variants = { list } > < motion . li variants = { item } /> < motion . li variants = { item } /> < motion . li variants = { item } /> </ motion . ul > )
```

### Orchestration

By default, this children animations will start simultaneously with the parent. But with variants we gain access to new transition props when and delayChildren .

```
transition
```

```
when
```

```
delayChildren
```

```
const list = { visible : { opacity : 1 , transition : { when : "beforeChildren" , delayChildren : stagger ( 0.3 ) , // Stagger children by .3 seconds } , } , hidden : { opacity : 0 , transition : { when : "afterChildren" , } , } , }
```

### Dynamic variants

Each variant can be defined as a function that resolves when a variant is made active.

```
const variants = { hidden : { opacity : 0 } , visible : ( index ) => ( { opacity : 1 , transition : { delay : index * 0.3 } } ) }
```

These functions are provided a single argument, which is passed via the custom prop:

```
custom
```

```
items . map ( ( item , index ) => < motion . div custom = { index } variants = { variants } /> )
```

This way, variants can be resolved differently for each animating element.

## Animation controls

Declarative animations via animate and whileHover cover most UI interactions. For cases that need sequencing, timeline scrubbing, or triggering animations from events outside React's render cycle, the useAnimate hook provides imperative controls:

```
animate
```

```
whileHover
```

```
useAnimate
```

- Animating any HTML/SVG element (not just motion components).

Animating any HTML/SVG element (not just motion components).

```
motion
```

- Complex animation sequences.

Complex animation sequences.

- Controlling animations with time , speed , play() , pause() and other playback controls.

Controlling animations with time , speed , play() , pause() and other playback controls.

```
time
```

```
speed
```

```
play()
```

```
pause()
```

```
function MyComponent ( ) { const [ scope , animate ] = useAnimate ( ) useEffect ( ( ) => { const controls = animate ( [ [ scope . current , { x : "100%" } ] , [ "li" , { opacity : 1 } ] ] ) controls . speed = 0.8 return ( ) => controls . stop ( ) } , [ ] ) return ( < ul ref = { scope } > < li /> < li /> < li /> </ ul > ) }
```

## Animate content

By passing a MotionValue as the child of a motion component, it will render its latest value in the HTML.

```
MotionValue
```

```
motion
```

```
import { useMotionValue , motion , animate } from "motion/react" function Counter ( ) { const count = useMotionValue ( 0 ) useEffect ( ( ) => { const controls = animate ( count , 100 , { duration : 5 } ) return ( ) => controls . stop ( ) } , [ ] ) return < motion . pre > { count } </ motion . pre > }
```

This avoids React re-renders entirely. The motion component updates the DOM text node directly, making it suitable for high-frequency value changes like counters or live data.

```
motion
```

It's also possible to animate numbers with a ticking counter effect using the AnimateNumber component in Motion+ by passing them directly to the component:

```
AnimateNumber
```

```
< AnimateNumber > { value } </ AnimateNumber >
```

## Next

In this guide we've covered the basic kinds of animations we can perform in Motion using its animation props . However, there's much more to discover.

Most of the examples on this page have used HTML elements, but Motion also has unique SVG animation features, like its simple line drawing API.

We've also only covered time-based animations, but Motion also provides powerful scroll animation features like useScroll and whileInView .

```
useScroll
```

```
whileInView
```

It also provides a powerful layout animation engine, that can animate between any two layouts using performant transforms.

Finally, there's also a whole Fundamentals examples category that covers all the basics of animating with Motion for React with live demos and copy-paste code.

Motion for React is a simple yet powerful animation library. Whether you're building hover effects, scroll-triggered animations, or complex animation sequences, this guide will provide an overview of all the ways you can animate in React with Motion.

## What you'll learn

- How to create your first animation with the <motion.div /> component.

How to create your first animation with the <motion.div /> component.

```
<motion.div />
```

- Which values and elements you can animate.

Which values and elements you can animate.

- How to customise your animations with transition options.

How to customise your animations with transition options.

- How to animate elements as they enter and exit the DOM.

How to animate elements as they enter and exit the DOM.

- How to orchestrate animations with variants.

How to orchestrate animations with variants.

If you haven't installed Motion already, hop over to the quick start guide for full instructions .

## Animate with <motion />

```
<motion />
```

Most animations in Motion are created with the <motion /> component . Import it from "motion/react" :

```
<motion />
```

```
"motion/react"
```

```
import { motion } from "motion/react"
```

Every HTML & SVG element can be defined with a motion component:

```
motion
```

```
< motion . div />
```

```
< motion . a href = "#" />
```

```
< motion . circle cx = { 0 } />
```

These work identically to their HTML/SVG counterparts - same props, same behaviour - but with additional animation props like animate , whileHover , and exit .

```
animate
```

```
whileHover
```

```
exit
```

The most common animation prop is animate . When values passed to animate change, the element will automatically animate to that value.

```
animate
```

```
animate
```

```
< motion . div animate = { { opacity : 1 } } />
```

### Enter animations

We can set initial values for an element with the initial prop. So an element defined like this will fade in when it enters the DOM:

```
initial
```

```
< motion . article initial = { { opacity : 0 } } animate = { { opacity : 1 } } />
```

## Animatable values

Motion can animate any CSS value , like opacity , filter etc.

```
opacity
```

```
filter
```

```
< motion . section initial = { { filter : "blur(10px)" } } animate = { { filter : "none" } } />
```

It can even animate values that aren't normally animatable by browsers, like background-image or mask-image :

```
background-image
```

```
mask-image
```

```
< motion . nav initial = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,0) 100%)" } } animate = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,1) 100%)" } } />
```

### Transforms

Unlike CSS, Motion can animate every transform axis independently.

```
< motion . div animate = { { x : 100 } } />
```

It supports the following special transform values:

- Translate: x , y , z

Translate: x , y , z

```
x
```

```
y
```

```
z
```

- Scale: scale , scaleX , scaleY

Scale: scale , scaleX , scaleY

```
scale
```

```
scaleX
```

```
scaleY
```

- Rotate: rotate , rotateX , rotateY , rotateZ

Rotate: rotate , rotateX , rotateY , rotateZ

```
rotate
```

```
rotateX
```

```
rotateY
```

```
rotateZ
```

- Skew: skewX , skewY

Skew: skewX , skewY

```
skewX
```

```
skewY
```

- Perspective: transformPerspective

Perspective: transformPerspective

```
transformPerspective
```

motion components also have enhanced style props, allowing you to use these shorthands statically:

```
motion
```

```
style
```

```
< motion . section style = { { x : - 20 } } />
```

Animating transforms independently provides great flexibility, especially when animating different transforms with gestures:

```
< motion . button initial = { { y : 10 } } animate = { { y : 0 } } whileHover = { { scale : 1.1 } } whileTap = { { scale : 0.9 } } />
```

Independent transforms already perform great, but Motion uniquely offers hardware acceleration when setting transform directly.

```
transform
```

```
< motion . li initial = { { transform : "translateX(-100px)" } } animate = { { transform : "translateX(0px)" } } transition = { { type : "spring" } } />
```

For SVG components, x and y attributes can be set using attrX and attrY . Learn more about SVG animations in React .

```
x
```

```
y
```

```
attrX
```

```
attrY
```

### Supported value types

Motion can animate any of the following value types:

- Numbers: 0 , 100 etc.

Numbers: 0 , 100 etc.

```
0
```

```
100
```

- Strings containing numbers: "0vh" , "10px" etc.

Strings containing numbers: "0vh" , "10px" etc.

```
"0vh"
```

```
"10px"
```

- Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

```
rgba
```

```
hsla
```

```
oklch
```

```
oklab
```

```
color-mix
```

- Complex strings containing multiple numbers and/or colors (like box-shadow ).

Complex strings containing multiple numbers and/or colors (like box-shadow ).

```
box-shadow
```

- display: "none"/"block" and visibility: "hidden"/"visible" .

display: "none"/"block" and visibility: "hidden"/"visible" .

```
display: "none"/"block"
```

```
visibility: "hidden"/"visible"
```

### Value type conversion

In general, values can only be animated between two of the same type (i.e "0px" to "100px" ).

```
"0px"
```

```
"100px"
```

Colors can be freely animated between hex, RGBA and HSLA types.

Additionally, x , y , width , height , top , left , right and bottom can animate between different value types.

```
x
```

```
y
```

```
width
```

```
height
```

```
top
```

```
left
```

```
right
```

```
bottom
```

```
< motion . div initial = { { x : "100%" } } animate = { { x : "calc(100vw - 50%)" } } />
```

It's also possible to animate width and height in to/out of "auto" .

```
width
```

```
height
```

```
"auto"
```

```
< motion . div initial = { { height : 0 } } animate = { { height : "auto" } } />
```

If animating height: auto while also animating display in to/out of "none" , replace this with visibility "hidden" as elements with display: none can't be measured.

```
height: auto
```

```
display
```

```
"none"
```

```
visibility
```

```
"hidden"
```

```
display: none
```

### Transform origin

transform-origin has three shortcut values that can be set and animated individually:

```
transform-origin
```

- originX

originX

```
originX
```

- originY

originY

```
originY
```

- originZ

originZ

```
originZ
```

If set as numbers, originX and Y default to a progress value between 0 and 1 . originZ defaults to pixels.

```
originX
```

```
Y
```

```
0
```

```
1
```

```
originZ
```

```
< motion . div style = { { originX : 0.5 } } />
```

### CSS variables

Motion for React can animate CSS variables, and also use CSS variable definitions as animation targets.

#### Animating CSS variables

Sometimes it's convenient to be able to animate a CSS variable to animate many children:

```
< motion . ul initial = { { '--rotate' : '0deg' } } animate = { { '--rotate' : '360deg' } } transition = { { duration : 2 , repeat : Infinity } } > < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> </ motion . ul >
```

Animating the value of a CSS variable always triggers paint , therefore it can be more performant to use MotionValue s to setup this kind of animation. Learn more about web animation performance .

```
MotionValue
```

#### Check your MotionScore

Enter a URL to audit your site's animation performance.

Check

### CSS variables as animation targets

HTML motion components accept animation targets with CSS variables:

```
motion
```

```
< motion . li animate = { { backgroundColor : "var(--action-bg)" } } />
```

## Transitions

By default, Motion will create appropriate transitions for snappy animations based on the type of value being animated.

For instance, physical properties like x or scale are animated with spring physics, whereas values like opacity or color are animated with duration-based easing curves.

```
x
```

```
scale
```

```
opacity
```

```
color
```

However, you can define your own animations via the transition prop .

```
transition
```

```
< motion . div animate = { { x : 100 } } transition = { { ease : "easeOut" , duration : 2 } } />
```

A default transition can be set for many components with the MotionConfig component :

```
transition
```

```
MotionConfig
```

```
< MotionConfig transition = { { duration : 0.3 } } > < motion . div animate = { { opacity : 1 } } />
```

Or you can set a specific transition on any animation prop:

```
transition
```

```
< motion . div animate = { { opacity : 1 } } whileHover = { { opacity : 0.7 , // Specific transitions override default transitions transition : { duration : 0.3 } } } transition = { { duration : 0.5 } } />
```

## Enter animations

When a motion component is first created, it'll automatically animate to the values in animate if they're different from those initially rendered, which you can either do via CSS or via the initial prop.

```
motion
```

```
animate
```

```
initial
```

```
< motion . li initial = { { opacity : 0 , scale : 0 } } animate = { { opacity : 1 , scale : 1 } } />
```

You can also disable the enter animation entirely by setting initial={false} . This will make the element render with the values defined in animate .

```
initial={false}
```

```
animate
```

```
< motion . div initial = { false } animate = { { y : 100 } } />
```

## Exit animations

Motion for React can animate elements as they're removed from the DOM.

In React, when a component is removed, it's usually removed instantly. Motion provides the AnimatePresence component which keeps elements in the DOM while they perform an animation defined with the exit prop.

```
AnimatePresence
```

```
exit
```

```
< AnimatePresence > { isVisible && ( < motion . div key = "modal" initial = { { opacity : 0 } } animate = { { opacity : 1 } } exit = { { opacity : 0 } } /> ) } </ AnimatePresence >
```

## Keyframes

So far, we've set animation props like animate and exit to single values, like opacity: 0 .

```
animate
```

```
exit
```

```
opacity: 0
```

This is great when we want to animate from the current value to a new value. But sometimes we want to animate through a series of values . In animation terms, these are called keyframes .

All animation props can accept keyframe arrays:

```
< motion . div animate = { { x : [ 0 , 100 , 0 ] } } />
```

When we animate to an array of values, the element will animate through each of these values in sequence.

In the previous example, we explicitly set the initial value as 0 . But we can also say "use the current value" by setting the first value to null .

```
0
```

```
null
```

```
< motion . div animate = { { x : [ null , 100 , 0 ] } } />
```

This way, if a keyframe animation is interrupting another animation, the transition will feel more natural.

### Wildcard keyframes

This null keyframe is called a wildcard keyframe . A wildcard keyframe simply takes the value before it (or the current value, if this is the first keyframe in the array).

```
null
```

Wildcard keyframes can be useful for holding a value mid-animation without having to repeat values.

```
< motion . div animate = { { x : [ 0 , 100 , null , 0 ] } } // same as x: [0, 100, 100, 0] but easier to maintain />
```

### Keyframe timing

By default, each keyframe is spaced evenly throughout the animation. You can override this by setting the times option via transition .

```
times
```

```
transition
```

times is an array of progress values between 0 and 1 , defining where in the animation each keyframe should be positioned.

```
times
```

```
0
```

```
1
```

```
< motion . circle cx = { 500 } animate = { { cx : [ null , 100 , 200 ] , transition : { duration : 3 , times : [ 0 , 0.2 , 1 ] } } } />
```

0 is the start of the animation, and 1 is the end of the animation. Therefore, 0.2 places this keyframe somewhere towards the start of the animation.

```
0
```

```
1
```

```
0.2
```

#### Stay in the loop

Sign up for the Motion newsletter.

Subscribe

## Gesture animations

Motion for React has animation props that can define how an element animates when it recognises a gesture .

Supported gestures are:

- whileHover

whileHover

```
whileHover
```

- whileTap

whileTap

```
whileTap
```

- whileFocus

whileFocus

```
whileFocus
```

- whileDrag

whileDrag

```
whileDrag
```

- whileInView

whileInView

```
whileInView
```

When a gesture starts, it animates to the values defined in while- , and then when the gesture ends it animates back to the values in initial or animate .

```
while-
```

```
initial
```

```
animate
```

```
< motion . button initial = { { opacity : 0 } } whileHover = { { backgroundColor : "rgba(220, 220, 220, 1)" } } whileTap = { { backgroundColor : "rgba(255, 255, 255, 1)" } } whileInView = { { opacity : 1 } } />
```

The custom Cursor component available in Motion+ takes this a step further with magnetic and target-morphing effects as a user hovers clickable targets (like buttons and links):

```
< Cursor magnetic />
```

## Variants

The animate prop works well for single elements, but real interfaces often need coordinated animations across parent and child components. Variants solve this by defining named animation states that propagate through the component tree.

```
animate
```

Variants are a set of named targets. These names can be anything.

```
const variants = { visible : { opacity : 1 } , hidden : { opacity : 0 } , }
```

Variants are passed to motion components via the variants prop:

```
motion
```

```
variants
```

```
< motion . div variants = { variants } />
```

These variants can now be referred to by a label, wherever you can define an animation target:

```
< motion . div variants = { variants } initial = "hidden" whileInView = "visible" exit = "hidden" />
```

You can also define multiple variants via an array:

```
animate = { [ "visible" , "danger" ] }
```

### Propagation

Variants are useful for reusing and combining animation targets. But it becomes powerful for orchestrating animations throughout trees.

Variants will flow down through motion components. So in this example when the ul enters the viewport, all of its children with a "visible" variant will also animate in:

```
motion
```

```
ul
```

```
const list = { visible : { opacity : 1 } , hidden : { opacity : 0 } , } const item = { visible : { opacity : 1 , x : 0 } , hidden : { opacity : 0 , x : - 100 } , } return ( < motion . ul initial = "hidden" whileInView = "visible" variants = { list } > < motion . li variants = { item } /> < motion . li variants = { item } /> < motion . li variants = { item } /> </ motion . ul > )
```

### Orchestration

By default, this children animations will start simultaneously with the parent. But with variants we gain access to new transition props when and delayChildren .

```
transition
```

```
when
```

```
delayChildren
```

```
const list = { visible : { opacity : 1 , transition : { when : "beforeChildren" , delayChildren : stagger ( 0.3 ) , // Stagger children by .3 seconds } , } , hidden : { opacity : 0 , transition : { when : "afterChildren" , } , } , }
```

### Dynamic variants

Each variant can be defined as a function that resolves when a variant is made active.

```
const variants = { hidden : { opacity : 0 } , visible : ( index ) => ( { opacity : 1 , transition : { delay : index * 0.3 } } ) }
```

These functions are provided a single argument, which is passed via the custom prop:

```
custom
```

```
items . map ( ( item , index ) => < motion . div custom = { index } variants = { variants } /> )
```

This way, variants can be resolved differently for each animating element.

## Animation controls

Declarative animations via animate and whileHover cover most UI interactions. For cases that need sequencing, timeline scrubbing, or triggering animations from events outside React's render cycle, the useAnimate hook provides imperative controls:

```
animate
```

```
whileHover
```

```
useAnimate
```

- Animating any HTML/SVG element (not just motion components).

Animating any HTML/SVG element (not just motion components).

```
motion
```

- Complex animation sequences.

Complex animation sequences.

- Controlling animations with time , speed , play() , pause() and other playback controls.

Controlling animations with time , speed , play() , pause() and other playback controls.

```
time
```

```
speed
```

```
play()
```

```
pause()
```

```
function MyComponent ( ) { const [ scope , animate ] = useAnimate ( ) useEffect ( ( ) => { const controls = animate ( [ [ scope . current , { x : "100%" } ] , [ "li" , { opacity : 1 } ] ] ) controls . speed = 0.8 return ( ) => controls . stop ( ) } , [ ] ) return ( < ul ref = { scope } > < li /> < li /> < li /> </ ul > ) }
```

## Animate content

By passing a MotionValue as the child of a motion component, it will render its latest value in the HTML.

```
MotionValue
```

```
motion
```

```
import { useMotionValue , motion , animate } from "motion/react" function Counter ( ) { const count = useMotionValue ( 0 ) useEffect ( ( ) => { const controls = animate ( count , 100 , { duration : 5 } ) return ( ) => controls . stop ( ) } , [ ] ) return < motion . pre > { count } </ motion . pre > }
```

This avoids React re-renders entirely. The motion component updates the DOM text node directly, making it suitable for high-frequency value changes like counters or live data.

```
motion
```

It's also possible to animate numbers with a ticking counter effect using the AnimateNumber component in Motion+ by passing them directly to the component:

```
AnimateNumber
```

```
< AnimateNumber > { value } </ AnimateNumber >
```

## Next

In this guide we've covered the basic kinds of animations we can perform in Motion using its animation props . However, there's much more to discover.

Most of the examples on this page have used HTML elements, but Motion also has unique SVG animation features, like its simple line drawing API.

We've also only covered time-based animations, but Motion also provides powerful scroll animation features like useScroll and whileInView .

```
useScroll
```

```
whileInView
```

It also provides a powerful layout animation engine, that can animate between any two layouts using performant transforms.

Finally, there's also a whole Fundamentals examples category that covers all the basics of animating with Motion for React with live demos and copy-paste code.

Motion for React is a simple yet powerful animation library. Whether you're building hover effects, scroll-triggered animations, or complex animation sequences, this guide will provide an overview of all the ways you can animate in React with Motion.

## What you'll learn

- How to create your first animation with the <motion.div /> component.

How to create your first animation with the <motion.div /> component.

```
<motion.div />
```

- Which values and elements you can animate.

Which values and elements you can animate.

- How to customise your animations with transition options.

How to customise your animations with transition options.

- How to animate elements as they enter and exit the DOM.

How to animate elements as they enter and exit the DOM.

- How to orchestrate animations with variants.

How to orchestrate animations with variants.

If you haven't installed Motion already, hop over to the quick start guide for full instructions .

## Animate with <motion />

```
<motion />
```

Most animations in Motion are created with the <motion /> component . Import it from "motion/react" :

```
<motion />
```

```
"motion/react"
```

```
import { motion } from "motion/react"
```

Every HTML & SVG element can be defined with a motion component:

```
motion
```

```
< motion . div />
```

```
< motion . a href = "#" />
```

```
< motion . circle cx = { 0 } />
```

These work identically to their HTML/SVG counterparts - same props, same behaviour - but with additional animation props like animate , whileHover , and exit .

```
animate
```

```
whileHover
```

```
exit
```

The most common animation prop is animate . When values passed to animate change, the element will automatically animate to that value.

```
animate
```

```
animate
```

```
< motion . div animate = { { opacity : 1 } } />
```

### Enter animations

We can set initial values for an element with the initial prop. So an element defined like this will fade in when it enters the DOM:

```
initial
```

```
< motion . article initial = { { opacity : 0 } } animate = { { opacity : 1 } } />
```

## Animatable values

Motion can animate any CSS value , like opacity , filter etc.

```
opacity
```

```
filter
```

```
< motion . section initial = { { filter : "blur(10px)" } } animate = { { filter : "none" } } />
```

It can even animate values that aren't normally animatable by browsers, like background-image or mask-image :

```
background-image
```

```
mask-image
```

```
< motion . nav initial = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,0) 100%)" } } animate = { { maskImage : "linear-gradient(to right, rgba(0,0,0,1) 90%, rgba(0,0,0,1) 100%)" } } />
```

### Transforms

Unlike CSS, Motion can animate every transform axis independently.

```
< motion . div animate = { { x : 100 } } />
```

It supports the following special transform values:

- Translate: x , y , z

Translate: x , y , z

```
x
```

```
y
```

```
z
```

- Scale: scale , scaleX , scaleY

Scale: scale , scaleX , scaleY

```
scale
```

```
scaleX
```

```
scaleY
```

- Rotate: rotate , rotateX , rotateY , rotateZ

Rotate: rotate , rotateX , rotateY , rotateZ

```
rotate
```

```
rotateX
```

```
rotateY
```

```
rotateZ
```

- Skew: skewX , skewY

Skew: skewX , skewY

```
skewX
```

```
skewY
```

- Perspective: transformPerspective

Perspective: transformPerspective

```
transformPerspective
```

motion components also have enhanced style props, allowing you to use these shorthands statically:

```
motion
```

```
style
```

```
< motion . section style = { { x : - 20 } } />
```

Animating transforms independently provides great flexibility, especially when animating different transforms with gestures:

```
< motion . button initial = { { y : 10 } } animate = { { y : 0 } } whileHover = { { scale : 1.1 } } whileTap = { { scale : 0.9 } } />
```

Independent transforms already perform great, but Motion uniquely offers hardware acceleration when setting transform directly.

```
transform
```

```
< motion . li initial = { { transform : "translateX(-100px)" } } animate = { { transform : "translateX(0px)" } } transition = { { type : "spring" } } />
```

For SVG components, x and y attributes can be set using attrX and attrY . Learn more about SVG animations in React .

```
x
```

```
y
```

```
attrX
```

```
attrY
```

### Supported value types

Motion can animate any of the following value types:

- Numbers: 0 , 100 etc.

Numbers: 0 , 100 etc.

```
0
```

```
100
```

- Strings containing numbers: "0vh" , "10px" etc.

Strings containing numbers: "0vh" , "10px" etc.

```
"0vh"
```

```
"10px"
```

- Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

Colors: All CSS color formats like hex, rgba , hsla , oklch , oklab , color-mix etc.

```
rgba
```

```
hsla
```

```
oklch
```

```
oklab
```

```
color-mix
```

- Complex strings containing multiple numbers and/or colors (like box-shadow ).

Complex strings containing multiple numbers and/or colors (like box-shadow ).

```
box-shadow
```

- display: "none"/"block" and visibility: "hidden"/"visible" .

display: "none"/"block" and visibility: "hidden"/"visible" .

```
display: "none"/"block"
```

```
visibility: "hidden"/"visible"
```

### Value type conversion

In general, values can only be animated between two of the same type (i.e "0px" to "100px" ).

```
"0px"
```

```
"100px"
```

Colors can be freely animated between hex, RGBA and HSLA types.

Additionally, x , y , width , height , top , left , right and bottom can animate between different value types.

```
x
```

```
y
```

```
width
```

```
height
```

```
top
```

```
left
```

```
right
```

```
bottom
```

```
< motion . div initial = { { x : "100%" } } animate = { { x : "calc(100vw - 50%)" } } />
```

It's also possible to animate width and height in to/out of "auto" .

```
width
```

```
height
```

```
"auto"
```

```
< motion . div initial = { { height : 0 } } animate = { { height : "auto" } } />
```

If animating height: auto while also animating display in to/out of "none" , replace this with visibility "hidden" as elements with display: none can't be measured.

```
height: auto
```

```
display
```

```
"none"
```

```
visibility
```

```
"hidden"
```

```
display: none
```

### Transform origin

transform-origin has three shortcut values that can be set and animated individually:

```
transform-origin
```

- originX

originX

```
originX
```

- originY

originY

```
originY
```

- originZ

originZ

```
originZ
```

If set as numbers, originX and Y default to a progress value between 0 and 1 . originZ defaults to pixels.

```
originX
```

```
Y
```

```
0
```

```
1
```

```
originZ
```

```
< motion . div style = { { originX : 0.5 } } />
```

### CSS variables

Motion for React can animate CSS variables, and also use CSS variable definitions as animation targets.

#### Animating CSS variables

Sometimes it's convenient to be able to animate a CSS variable to animate many children:

```
< motion . ul initial = { { '--rotate' : '0deg' } } animate = { { '--rotate' : '360deg' } } transition = { { duration : 2 , repeat : Infinity } } > < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> < li style = { { transform : 'rotate(var(--rotate))' } } /> </ motion . ul >
```

Animating the value of a CSS variable always triggers paint , therefore it can be more performant to use MotionValue s to setup this kind of animation. Learn more about web animation performance .

```
MotionValue
```

#### Check your MotionScore

Enter a URL to audit your site's animation performance.

Check

### CSS variables as animation targets

HTML motion components accept animation targets with CSS variables:

```
motion
```

```
< motion . li animate = { { backgroundColor : "var(--action-bg)" } } />
```

## Transitions

By default, Motion will create appropriate transitions for snappy animations based on the type of value being animated.

For instance, physical properties like x or scale are animated with spring physics, whereas values like opacity or color are animated with duration-based easing curves.

```
x
```

```
scale
```

```
opacity
```

```
color
```

However, you can define your own animations via the transition prop .

```
transition
```

```
< motion . div animate = { { x : 100 } } transition = { { ease : "easeOut" , duration : 2 } } />
```

A default transition can be set for many components with the MotionConfig component :

```
transition
```

```
MotionConfig
```

```
< MotionConfig transition = { { duration : 0.3 } } > < motion . div animate = { { opacity : 1 } } />
```

Or you can set a specific transition on any animation prop:

```
transition
```

```
< motion . div animate = { { opacity : 1 } } whileHover = { { opacity : 0.7 , // Specific transitions override default transitions transition : { duration : 0.3 } } } transition = { { duration : 0.5 } } />
```

## Enter animations

When a motion component is first created, it'll automatically animate to the values in animate if they're different from those initially rendered, which you can either do via CSS or via the initial prop.

```
motion
```

```
animate
```

```
initial
```

```
< motion . li initial = { { opacity : 0 , scale : 0 } } animate = { { opacity : 1 , scale : 1 } } />
```

You can also disable the enter animation entirely by setting initial={false} . This will make the element render with the values defined in animate .

```
initial={false}
```

```
animate
```

```
< motion . div initial = { false } animate = { { y : 100 } } />
```

## Exit animations

Motion for React can animate elements as they're removed from the DOM.

In React, when a component is removed, it's usually removed instantly. Motion provides the AnimatePresence component which keeps elements in the DOM while they perform an animation defined with the exit prop.

```
AnimatePresence
```

```
exit
```

```
< AnimatePresence > { isVisible && ( < motion . div key = "modal" initial = { { opacity : 0 } } animate = { { opacity : 1 } } exit = { { opacity : 0 } } /> ) } </ AnimatePresence >
```

## Keyframes

So far, we've set animation props like animate and exit to single values, like opacity: 0 .

```
animate
```

```
exit
```

```
opacity: 0
```

This is great when we want to animate from the current value to a new value. But sometimes we want to animate through a series of values . In animation terms, these are called keyframes .

All animation props can accept keyframe arrays:

```
< motion . div animate = { { x : [ 0 , 100 , 0 ] } } />
```

When we animate to an array of values, the element will animate through each of these values in sequence.

In the previous example, we explicitly set the initial value as 0 . But we can also say "use the current value" by setting the first value to null .

```
0
```

```
null
```

```
< motion . div animate = { { x : [ null , 100 , 0 ] } } />
```

This way, if a keyframe animation is interrupting another animation, the transition will feel more natural.

### Wildcard keyframes

This null keyframe is called a wildcard keyframe . A wildcard keyframe simply takes the value before it (or the current value, if this is the first keyframe in the array).

```
null
```

Wildcard keyframes can be useful for holding a value mid-animation without having to repeat values.

```
< motion . div animate = { { x : [ 0 , 100 , null , 0 ] } } // same as x: [0, 100, 100, 0] but easier to maintain />
```

### Keyframe timing

By default, each keyframe is spaced evenly throughout the animation. You can override this by setting the times option via transition .

```
times
```

```
transition
```

times is an array of progress values between 0 and 1 , defining where in the animation each keyframe should be positioned.

```
times
```

```
0
```

```
1
```

```
< motion . circle cx = { 500 } animate = { { cx : [ null , 100 , 200 ] , transition : { duration : 3 , times : [ 0 , 0.2 , 1 ] } } } />
```

0 is the start of the animation, and 1 is the end of the animation. Therefore, 0.2 places this keyframe somewhere towards the start of the animation.

```
0
```

```
1
```

```
0.2
```

#### Stay in the loop

Sign up for the Motion newsletter.

Subscribe

## Gesture animations

Motion for React has animation props that can define how an element animates when it recognises a gesture .

Supported gestures are:

- whileHover

whileHover

```
whileHover
```

- whileTap

whileTap

```
whileTap
```

- whileFocus

whileFocus

```
whileFocus
```

- whileDrag

whileDrag

```
whileDrag
```

- whileInView

whileInView

```
whileInView
```

When a gesture starts, it animates to the values defined in while- , and then when the gesture ends it animates back to the values in initial or animate .

```
while-
```

```
initial
```

```
animate
```

```
< motion . button initial = { { opacity : 0 } } whileHover = { { backgroundColor : "rgba(220, 220, 220, 1)" } } whileTap = { { backgroundColor : "rgba(255, 255, 255, 1)" } } whileInView = { { opacity : 1 } } />
```

The custom Cursor component available in Motion+ takes this a step further with magnetic and target-morphing effects as a user hovers clickable targets (like buttons and links):

```
< Cursor magnetic />
```

## Variants

The animate prop works well for single elements, but real interfaces often need coordinated animations across parent and child components. Variants solve this by defining named animation states that propagate through the component tree.

```
animate
```

Variants are a set of named targets. These names can be anything.

```
const variants = { visible : { opacity : 1 } , hidden : { opacity : 0 } , }
```

Variants are passed to motion components via the variants prop:

```
motion
```

```
variants
```

```
< motion . div variants = { variants } />
```

These variants can now be referred to by a label, wherever you can define an animation target:

```
< motion . div variants = { variants } initial = "hidden" whileInView = "visible" exit = "hidden" />
```

You can also define multiple variants via an array:

```
animate = { [ "visible" , "danger" ] }
```

### Propagation

Variants are useful for reusing and combining animation targets. But it becomes powerful for orchestrating animations throughout trees.

Variants will flow down through motion components. So in this example when the ul enters the viewport, all of its children with a "visible" variant will also animate in:

```
motion
```

```
ul
```

```
const list = { visible : { opacity : 1 } , hidden : { opacity : 0 } , } const item = { visible : { opacity : 1 , x : 0 } , hidden : { opacity : 0 , x : - 100 } , } return ( < motion . ul initial = "hidden" whileInView = "visible" variants = { list } > < motion . li variants = { item } /> < motion . li variants = { item } /> < motion . li variants = { item } /> </ motion . ul > )
```

### Orchestration

By default, this children animations will start simultaneously with the parent. But with variants we gain access to new transition props when and delayChildren .

```
transition
```

```
when
```

```
delayChildren
```

```
const list = { visible : { opacity : 1 , transition : { when : "beforeChildren" , delayChildren : stagger ( 0.3 ) , // Stagger children by .3 seconds } , } , hidden : { opacity : 0 , transition : { when : "afterChildren" , } , } , }
```

### Dynamic variants

Each variant can be defined as a function that resolves when a variant is made active.

```
const variants = { hidden : { opacity : 0 } , visible : ( index ) => ( { opacity : 1 , transition : { delay : index * 0.3 } } ) }
```

These functions are provided a single argument, which is passed via the custom prop:

```
custom
```

```
items . map ( ( item , index ) => < motion . div custom = { index } variants = { variants } /> )
```

This way, variants can be resolved differently for each animating element.

## Animation controls

Declarative animations via animate and whileHover cover most UI interactions. For cases that need sequencing, timeline scrubbing, or triggering animations from events outside React's render cycle, the useAnimate hook provides imperative controls:

```
animate
```

```
whileHover
```

```
useAnimate
```

- Animating any HTML/SVG element (not just motion components).

Animating any HTML/SVG element (not just motion components).

```
motion
```

- Complex animation sequences.

Complex animation sequences.

- Controlling animations with time , speed , play() , pause() and other playback controls.

Controlling animations with time , speed , play() , pause() and other playback controls.

```
time
```

```
speed
```

```
play()
```

```
pause()
```

```
function MyComponent ( ) { const [ scope , animate ] = useAnimate ( ) useEffect ( ( ) => { const controls = animate ( [ [ scope . current , { x : "100%" } ] , [ "li" , { opacity : 1 } ] ] ) controls . speed = 0.8 return ( ) => controls . stop ( ) } , [ ] ) return ( < ul ref = { scope } > < li /> < li /> < li /> </ ul > ) }
```

## Animate content

By passing a MotionValue as the child of a motion component, it will render its latest value in the HTML.

```
MotionValue
```

```
motion
```

```
import { useMotionValue , motion , animate } from "motion/react" function Counter ( ) { const count = useMotionValue ( 0 ) useEffect ( ( ) => { const controls = animate ( count , 100 , { duration : 5 } ) return ( ) => controls . stop ( ) } , [ ] ) return < motion . pre > { count } </ motion . pre > }
```

This avoids React re-renders entirely. The motion component updates the DOM text node directly, making it suitable for high-frequency value changes like counters or live data.

```
motion
```

It's also possible to animate numbers with a ticking counter effect using the AnimateNumber component in Motion+ by passing them directly to the component:

```
AnimateNumber
```

```
< AnimateNumber > { value } </ AnimateNumber >
```

## Next

In this guide we've covered the basic kinds of animations we can perform in Motion using its animation props . However, there's much more to discover.

Most of the examples on this page have used HTML elements, but Motion also has unique SVG animation features, like its simple line drawing API.

We've also only covered time-based animations, but Motion also provides powerful scroll animation features like useScroll and whileInView .

```
useScroll
```

```
whileInView
```

It also provides a powerful layout animation engine, that can animate between any two layouts using performant transforms.

Finally, there's also a whole Fundamentals examples category that covers all the basics of animating with Motion for React with live demos and copy-paste code.

## Related topics

- AI Context Give your AI editor Motion docs, 330+ examples, and transition tools via MCP. AI Context Give your AI editor Motion docs, 330+ examples, and transition tools via MCP.

### AI Context

Give your AI editor Motion docs, 330+ examples, and transition tools via MCP.

### AI Context

Give your AI editor Motion docs, 330+ examples, and transition tools via MCP.

- Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations. Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations.

### Motion component

Animate elements with a declarative API. Supports variants, gestures, and layout animations.

### Motion component

Animate elements with a declarative API. Supports variants, gestures, and layout animations.

- React scroll animation Create scroll-triggered and scroll-linked effects â parallax, progress and more. React scroll animation Create scroll-triggered and scroll-linked effects â parallax, progress and more.

### React scroll animation

Create scroll-triggered and scroll-linked effects â parallax, progress and more.

### React scroll animation

Create scroll-triggered and scroll-linked effects â parallax, progress and more.

- Motion+ Cursor Create custom cursor and follow-along effects in React. Motion+ Cursor Create custom cursor and follow-along effects in React.

Motion+

### Cursor

Create custom cursor and follow-along effects in React.

Motion+

### Cursor

Create custom cursor and follow-along effects in React.

- Tutorial Transition options An example of setting transition options in Motion for React.

Tutorial

### Transition options

An example of setting transition options in Motion for React.

- Tutorial Transition options An example of setting transition options in Motion for React.

Tutorial

### Transition options

An example of setting transition options in Motion for React.

Previous

Get started with Motion for React

Next

Layout animation

Motion+

## Ready for the next step?

Learn more by unlocking the full vault of Motion+ pre-built animation examples. Ready to copy-paste directly into your project.

See Motion+ features & pricing

See Motion+ features & pricing

One-time payment, lifetime updates.

AI-ready animations

Make your LLM an animation expert with 330+ pre-built examples available via MCP.
