# SVG Animation in React â Paths, Morph & Line Drawing | Motion

Source: https://motion.dev/docs/react-svg-animation

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

# SVG animation

Motion makes React SVG animation straightforward. In this guide, we'll learn how to make line drawing animations, path morphing animations, animate viewBox and more.

```
viewBox
```

## Overview

SVG animations are performed via the motion component . There's a motion component for every SVG element (e.g. <motion.svg> , <motion.path> , <motion.circle> , and even filters like <motion.feTurbulence> and <motion.feDisplacementMap> ).

```
motion
```

```
motion
```

```
<motion.svg>
```

```
<motion.path>
```

```
<motion.circle>
```

```
<motion.feTurbulence>
```

```
<motion.feDisplacementMap>
```

```
< motion . svg > < motion . circle /> </ motion . svg >
```

A motion component can animate style , as normal:

```
motion
```

```
style
```

```
< motion . circle style = { { fill : "#00f" } } animate = { { fill : "#f00" } } />
```

But it can also animate attributes:

```
< motion . circle cx = { 0 } animate = { { cx : 50 } } />
```

### Animate viewBox

```
viewBox
```

The motion.svg component can additionally animate viewBox . This is especially useful for easy panning animations:

```
motion.svg
```

```
viewBox
```

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "100 0 200 200" } } // 100px to the right />
```

Or zoom in/out animations:

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "-100 -100 300 300" } } // Zoom out />
```

### Transforms

SVG transforms work differently to CSS transforms. When we define a CSS transform, the default origin is relative to the element itself. So for instance, this div will rotate around its center point, as you'd intuitively expect:

```
div
```

```
< motion . div style = { { rotate : 90 } } />
```

With SVGs, the transform point is relative to the top/left corner of the viewBox , which is less intuitive. Motion changes this behaviour so SVGs work the same as normal elements. Therefore, this:

```
viewBox
```

```
< motion . rect style = { { rotate : 90 } } />
```

Will also rotate the rect element around its center point.

```
rect
```

The default behaviour can be restored by explicitly setting an element's transformBox style:

```
transformBox
```

```
< motion . rect style = { { rotate : 90 , transformBox : "view-box" } } />
```

### x / y / scale attributes

```
x
```

```
y
```

```
scale
```

motion components provide shorthands for x , y , and scale transforms:

```
motion
```

```
x
```

```
y
```

```
scale
```

```
< motion . div animate = { { x : 100 } } />
```

With SVG components, these will still render via the style tag. This is usually fine, but some SVG components accept x , y , and scale attributes also. You can target these via animation props using attrX , attrY and attrScale respectively:

```
style
```

```
x
```

```
y
```

```
scale
```

```
attrX
```

```
attrY
```

```
attrScale
```

```
< motion . rect attrX = { 0 } animate = { { attrX : 100 } } />
```

#### Transition editor for IDEs

Perfect your CSS and Motion transitions, directly in your code editor.

### Passing MotionValue

```
MotionValue
```

Motion values should be passed via style , when animating regular styles, or via the component's attribute where appropriate:

```
style
```

```
const cx = useMotionValue ( 100 ) const opacity = useMotionValue ( 1 ) return < motion . rect cx = { cx } style = { { opacity } } />
```

## Line drawing

Motion simplifies the creation of âhand-drawnâ line animations using three special values. Each is set as a 0 - 1 progress value, where 1 is the total length of the line:

```
0
```

```
1
```

```
1
```

- pathLength : total drawn length

pathLength : total drawn length

```
pathLength
```

- pathSpacing : length between segments

pathSpacing : length between segments

```
pathSpacing
```

- pathOffset : where the segment starts

pathOffset : where the segment starts

```
pathOffset
```

These values work on path , circle , ellipse , line , polygon , polyline , rect .

```
path
```

```
circle
```

```
ellipse
```

```
line
```

```
polygon
```

```
polyline
```

```
rect
```

```
< motion . path d = { d } initial = { { pathLength : 0 } } animate = { { pathLength : 1 } } />
```

## Path morphing

It's possible to also animate the shape of a path via its d attribute.

```
path
```

```
d
```

```
< motion . path d = "M 0,0 l 0,10 l 10,10" animate = { { d : "M 0,0 l 10,0 l 10,10" } } />
```

This works natively in Motion as long as the two paths are similar . You can see in the example above that each path has the same number and type of path instructions.

For interpolating between very different paths, you can incorporate a third-party path mixer like Flubber :

## Drag gesture

SVG elements can be made draggable in the same way as their HTML counterparts, using the drag prop.

```
drag
```

```
< motion . circle drag />
```

However, it's possible that an SVG is rendered with a viewBox that is different from its rendered size.

```
viewBox
```

For example, this SVG has a viewBox of 100px width and height, vs a rendered size of 200px :

```
viewBox
```

```
100px
```

```
200px
```

```
< svg viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } />
```

This will conflict with the drag gesture. To fix, we can use the MotionConfig transformPagePoint prop to rescale pointer movements:

```
MotionConfig
```

```
transformPagePoint
```

```
import { motion , MotionConfig , transformViewBoxPoint } from "motion/react" function Component ( ) { const ref = useRef ( null ) return ( < MotionConfig transformPagePoint = { transformViewBoxPoint ( ref ) } > < svg ref = { ref } viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } > < motion . circle drag /> </ svg > </ MotionConfig > ) }
```

Motion makes React SVG animation straightforward. In this guide, we'll learn how to make line drawing animations, path morphing animations, animate viewBox and more.

```
viewBox
```

## Overview

SVG animations are performed via the motion component . There's a motion component for every SVG element (e.g. <motion.svg> , <motion.path> , <motion.circle> , and even filters like <motion.feTurbulence> and <motion.feDisplacementMap> ).

```
motion
```

```
motion
```

```
<motion.svg>
```

```
<motion.path>
```

```
<motion.circle>
```

```
<motion.feTurbulence>
```

```
<motion.feDisplacementMap>
```

```
< motion . svg > < motion . circle /> </ motion . svg >
```

A motion component can animate style , as normal:

```
motion
```

```
style
```

```
< motion . circle style = { { fill : "#00f" } } animate = { { fill : "#f00" } } />
```

But it can also animate attributes:

```
< motion . circle cx = { 0 } animate = { { cx : 50 } } />
```

### Animate viewBox

```
viewBox
```

The motion.svg component can additionally animate viewBox . This is especially useful for easy panning animations:

```
motion.svg
```

```
viewBox
```

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "100 0 200 200" } } // 100px to the right />
```

Or zoom in/out animations:

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "-100 -100 300 300" } } // Zoom out />
```

### Transforms

SVG transforms work differently to CSS transforms. When we define a CSS transform, the default origin is relative to the element itself. So for instance, this div will rotate around its center point, as you'd intuitively expect:

```
div
```

```
< motion . div style = { { rotate : 90 } } />
```

With SVGs, the transform point is relative to the top/left corner of the viewBox , which is less intuitive. Motion changes this behaviour so SVGs work the same as normal elements. Therefore, this:

```
viewBox
```

```
< motion . rect style = { { rotate : 90 } } />
```

Will also rotate the rect element around its center point.

```
rect
```

The default behaviour can be restored by explicitly setting an element's transformBox style:

```
transformBox
```

```
< motion . rect style = { { rotate : 90 , transformBox : "view-box" } } />
```

### x / y / scale attributes

```
x
```

```
y
```

```
scale
```

motion components provide shorthands for x , y , and scale transforms:

```
motion
```

```
x
```

```
y
```

```
scale
```

```
< motion . div animate = { { x : 100 } } />
```

With SVG components, these will still render via the style tag. This is usually fine, but some SVG components accept x , y , and scale attributes also. You can target these via animation props using attrX , attrY and attrScale respectively:

```
style
```

```
x
```

```
y
```

```
scale
```

```
attrX
```

```
attrY
```

```
attrScale
```

```
< motion . rect attrX = { 0 } animate = { { attrX : 100 } } />
```

#### Transition editor for IDEs

Perfect your CSS and Motion transitions, directly in your code editor.

### Passing MotionValue

```
MotionValue
```

Motion values should be passed via style , when animating regular styles, or via the component's attribute where appropriate:

```
style
```

```
const cx = useMotionValue ( 100 ) const opacity = useMotionValue ( 1 ) return < motion . rect cx = { cx } style = { { opacity } } />
```

## Line drawing

Motion simplifies the creation of âhand-drawnâ line animations using three special values. Each is set as a 0 - 1 progress value, where 1 is the total length of the line:

```
0
```

```
1
```

```
1
```

- pathLength : total drawn length

pathLength : total drawn length

```
pathLength
```

- pathSpacing : length between segments

pathSpacing : length between segments

```
pathSpacing
```

- pathOffset : where the segment starts

pathOffset : where the segment starts

```
pathOffset
```

These values work on path , circle , ellipse , line , polygon , polyline , rect .

```
path
```

```
circle
```

```
ellipse
```

```
line
```

```
polygon
```

```
polyline
```

```
rect
```

```
< motion . path d = { d } initial = { { pathLength : 0 } } animate = { { pathLength : 1 } } />
```

## Path morphing

It's possible to also animate the shape of a path via its d attribute.

```
path
```

```
d
```

```
< motion . path d = "M 0,0 l 0,10 l 10,10" animate = { { d : "M 0,0 l 10,0 l 10,10" } } />
```

This works natively in Motion as long as the two paths are similar . You can see in the example above that each path has the same number and type of path instructions.

For interpolating between very different paths, you can incorporate a third-party path mixer like Flubber :

## Drag gesture

SVG elements can be made draggable in the same way as their HTML counterparts, using the drag prop.

```
drag
```

```
< motion . circle drag />
```

However, it's possible that an SVG is rendered with a viewBox that is different from its rendered size.

```
viewBox
```

For example, this SVG has a viewBox of 100px width and height, vs a rendered size of 200px :

```
viewBox
```

```
100px
```

```
200px
```

```
< svg viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } />
```

This will conflict with the drag gesture. To fix, we can use the MotionConfig transformPagePoint prop to rescale pointer movements:

```
MotionConfig
```

```
transformPagePoint
```

```
import { motion , MotionConfig , transformViewBoxPoint } from "motion/react" function Component ( ) { const ref = useRef ( null ) return ( < MotionConfig transformPagePoint = { transformViewBoxPoint ( ref ) } > < svg ref = { ref } viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } > < motion . circle drag /> </ svg > </ MotionConfig > ) }
```

Motion makes React SVG animation straightforward. In this guide, we'll learn how to make line drawing animations, path morphing animations, animate viewBox and more.

```
viewBox
```

## Overview

SVG animations are performed via the motion component . There's a motion component for every SVG element (e.g. <motion.svg> , <motion.path> , <motion.circle> , and even filters like <motion.feTurbulence> and <motion.feDisplacementMap> ).

```
motion
```

```
motion
```

```
<motion.svg>
```

```
<motion.path>
```

```
<motion.circle>
```

```
<motion.feTurbulence>
```

```
<motion.feDisplacementMap>
```

```
< motion . svg > < motion . circle /> </ motion . svg >
```

A motion component can animate style , as normal:

```
motion
```

```
style
```

```
< motion . circle style = { { fill : "#00f" } } animate = { { fill : "#f00" } } />
```

But it can also animate attributes:

```
< motion . circle cx = { 0 } animate = { { cx : 50 } } />
```

### Animate viewBox

```
viewBox
```

The motion.svg component can additionally animate viewBox . This is especially useful for easy panning animations:

```
motion.svg
```

```
viewBox
```

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "100 0 200 200" } } // 100px to the right />
```

Or zoom in/out animations:

```
< motion . svg viewBox = "0 0 200 200" animate = { { viewBox : "-100 -100 300 300" } } // Zoom out />
```

### Transforms

SVG transforms work differently to CSS transforms. When we define a CSS transform, the default origin is relative to the element itself. So for instance, this div will rotate around its center point, as you'd intuitively expect:

```
div
```

```
< motion . div style = { { rotate : 90 } } />
```

With SVGs, the transform point is relative to the top/left corner of the viewBox , which is less intuitive. Motion changes this behaviour so SVGs work the same as normal elements. Therefore, this:

```
viewBox
```

```
< motion . rect style = { { rotate : 90 } } />
```

Will also rotate the rect element around its center point.

```
rect
```

The default behaviour can be restored by explicitly setting an element's transformBox style:

```
transformBox
```

```
< motion . rect style = { { rotate : 90 , transformBox : "view-box" } } />
```

### x / y / scale attributes

```
x
```

```
y
```

```
scale
```

motion components provide shorthands for x , y , and scale transforms:

```
motion
```

```
x
```

```
y
```

```
scale
```

```
< motion . div animate = { { x : 100 } } />
```

With SVG components, these will still render via the style tag. This is usually fine, but some SVG components accept x , y , and scale attributes also. You can target these via animation props using attrX , attrY and attrScale respectively:

```
style
```

```
x
```

```
y
```

```
scale
```

```
attrX
```

```
attrY
```

```
attrScale
```

```
< motion . rect attrX = { 0 } animate = { { attrX : 100 } } />
```

#### Transition editor for IDEs

Perfect your CSS and Motion transitions, directly in your code editor.

### Passing MotionValue

```
MotionValue
```

Motion values should be passed via style , when animating regular styles, or via the component's attribute where appropriate:

```
style
```

```
const cx = useMotionValue ( 100 ) const opacity = useMotionValue ( 1 ) return < motion . rect cx = { cx } style = { { opacity } } />
```

## Line drawing

Motion simplifies the creation of âhand-drawnâ line animations using three special values. Each is set as a 0 - 1 progress value, where 1 is the total length of the line:

```
0
```

```
1
```

```
1
```

- pathLength : total drawn length

pathLength : total drawn length

```
pathLength
```

- pathSpacing : length between segments

pathSpacing : length between segments

```
pathSpacing
```

- pathOffset : where the segment starts

pathOffset : where the segment starts

```
pathOffset
```

These values work on path , circle , ellipse , line , polygon , polyline , rect .

```
path
```

```
circle
```

```
ellipse
```

```
line
```

```
polygon
```

```
polyline
```

```
rect
```

```
< motion . path d = { d } initial = { { pathLength : 0 } } animate = { { pathLength : 1 } } />
```

## Path morphing

It's possible to also animate the shape of a path via its d attribute.

```
path
```

```
d
```

```
< motion . path d = "M 0,0 l 0,10 l 10,10" animate = { { d : "M 0,0 l 10,0 l 10,10" } } />
```

This works natively in Motion as long as the two paths are similar . You can see in the example above that each path has the same number and type of path instructions.

For interpolating between very different paths, you can incorporate a third-party path mixer like Flubber :

## Drag gesture

SVG elements can be made draggable in the same way as their HTML counterparts, using the drag prop.

```
drag
```

```
< motion . circle drag />
```

However, it's possible that an SVG is rendered with a viewBox that is different from its rendered size.

```
viewBox
```

For example, this SVG has a viewBox of 100px width and height, vs a rendered size of 200px :

```
viewBox
```

```
100px
```

```
200px
```

```
< svg viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } />
```

This will conflict with the drag gesture. To fix, we can use the MotionConfig transformPagePoint prop to rescale pointer movements:

```
MotionConfig
```

```
transformPagePoint
```

```
import { motion , MotionConfig , transformViewBoxPoint } from "motion/react" function Component ( ) { const ref = useRef ( null ) return ( < MotionConfig transformPagePoint = { transformViewBoxPoint ( ref ) } > < svg ref = { ref } viewBox = "0 0 100 100" style = { { width : 200 , height : 200 } } > < motion . circle drag /> </ svg > </ MotionConfig > ) }
```

## Related topics

- Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations. Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations.

### Motion component

Animate elements with a declarative API. Supports variants, gestures, and layout animations.

### Motion component

Animate elements with a declarative API. Supports variants, gestures, and layout animations.

- Motion values overview Composable animatable values that can updated styles without re-renders. Motion values overview Composable animatable values that can updated styles without re-renders.

### Motion values overview

Composable animatable values that can updated styles without re-renders.

### Motion values overview

Composable animatable values that can updated styles without re-renders.

- React animation Create React animation with Motion components. Learn variants, gestures, and keyframes. React animation Create React animation with Motion components. Learn variants, gestures, and keyframes.

### React animation

Create React animation with Motion components. Learn variants, gestures, and keyframes.

### React animation

Create React animation with Motion components. Learn variants, gestures, and keyframes.

- Tutorial Path morphing An example of creating smooth SVG path morphing animations with Motion for React.

Tutorial

### Path morphing

An example of creating smooth SVG path morphing animations with Motion for React.

- Tutorial Path morphing An example of creating smooth SVG path morphing animations with Motion for React.

Tutorial

### Path morphing

An example of creating smooth SVG path morphing animations with Motion for React.

Previous

React scroll animation

Next

Transitions

Motion+

## Master layout animations

Unlock the full vault of 330+ Motion examples, 100+ tutorials, premium APIs, private Discord and GitHub, and powerful Motion Studio animation editing tools for your IDE.

Get Motion+

Get Motion+

One-time payment, lifetime updates.

AI-ready animations

Make your LLM an animation expert with 330+ pre-built examples available via MCP.
