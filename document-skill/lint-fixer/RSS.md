xml version="1.0" encoding="UTF-8"?Biome | Bloghttps://biomejs.dev/enBiome v2.4—Embedded Snippets, HTML Accessibility, and Better Framework Supporthttps://biomejs.dev/blog/biome-v2-4/https://biomejs.dev/blog/biome-v2-4/Biome 2.4 introduces embedded CSS and GraphQL formatting, 15 new HTML accessibility rules, significantly improved support for Vue, Svelte, and Astro, and promotes 24 rules to stable. Plus new CLI reporters, rule profiler, and editor configuration features.
Tue, 10 Feb 2026 00:00:00 GMT<p>Biome v2.4 is the first minor release of the year! After more than ten patches from v2.3, today we bring to you a new version that contains many new features!</p>
<p>Once you have upgraded to Biome v2.4.0, migrate your Biome configuration to the new version by running the <code dir="auto">migrate</code> command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="highlights">Highlights</h2></div>
<p>Among all the features shipped in this release, here are the ones we think you’re going to like most!</p>
<ul>
<li><a href="#embedded-snippets-in-javascript">Embedded snippets in JavaScript</a></li>
<li><a href="#editor-inline-configuration">Editor inline configuration</a></li>
<li><a href="#major-improvements-to-html-ish-languages">Major improvements to HTML-ish languages</a></li>
<li><a href="#html-accessibility-rules">HTML accessibility rules</a></li>
<li><a href="#rule-profiler">Rule profiler</a></li>
<li><a href="#configuration-file-discovery">Configuration file discovery</a></li>
</ul>
<div><h3 id="embedded-snippets-in-javascript">Embedded snippets in JavaScript</h3></div>
<p>One of the most significant new features in Biome 2.4 is the ability to format and lint embedded CSS and GraphQL snippets within JavaScript files. Enable this experimental feature to automatically format and lint CSS and GraphQL code within template literals.</p>
<p>Biome recognizes CSS snippets from styled-components, Emotion, and similar CSS-in-JS libraries:</p>
<div><figure><figcaption><span>styled-components.js</span></figcaption><pre><code><div><div><span>import</span><span> styled </span><span>from</span><span> </span><span>"</span><span>styled-components</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>const </span><span>Foo</span><span> = </span><span>styled</span><span>.</span><span>div</span><span>`</span></div></div><div><div><span><span> </span></span><span>display: flex;</span></div></div><div><div><span><span> </span></span><span>color: red;</span></div></div><div><div><span>`</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>GraphQL queries and mutations within JavaScript are now properly formatted and linted:</p>
<div><figure><figcaption><span>graphql-query.js</span></figcaption><pre><code><div><div><span>import</span><span> gql </span><span>from</span><span> </span><span>"</span><span>graphql-tag</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>const </span><span>PeopleCountQuery</span><span> = </span><span>gql</span><span>`</span></div></div><div><div><span><span> </span></span><span>query PeopleCount {</span></div></div><div><div><span><span> </span></span><span>allPeople {</span></div></div><div><div><span><span> </span></span><span>totalCount</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>`</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>To enable these features, add this to your configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"experimentalEmbeddedSnippetsEnabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<aside aria-label="Note"><p aria-hidden="true">Note</p><div><p>Snippets with interpolations are not yet supported.</p></div></aside>
<div><h3 id="editor-inline-configuration">Editor inline configuration</h3></div>
<p>Editors can now inject a Biome configuration to the Biome Language Server without affecting the project’s configuration.</p>
<p>If you have a Biome extension compatible with your LSP-ready editor, you can map <code dir="auto">inlineConfig</code>. The configuration will be merged with the project’s configuration and it will take precedence.</p>
<p>In the following example, the editor won’t emit any diagnostics for the rule <code dir="auto">noConsole</code>, but the CLI will still conform to the configuration of the project.</p>
<starlight-tabs data-sync-key="action"> <div> <ul role="tablist"> <li role="presentation"> <a role="tab" href="#tab-panel-138" id="tab-138" aria-selected="true" tabindex="0"> <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M2.25 1.5a.75.75 0 0 0-.75.75v16.5H0V2.25C0 1.01 1 0 2.25 0h20.1c1 0 1.5 1.21.79 1.92L10.76 14.3h3.49v-1.55h1.5v1.92c0 .62-.5 1.13-1.13 1.13H9.27L6.7 18.37h11.69V9h1.5v9.38c0 .82-.68 1.5-1.5 1.5H5.18L2.57 22.5h19.19c.41 0 .75-.34.75-.75V5.25H24v16.5c0 1.24-1 2.25-2.25 2.25H1.65c-1 0-1.5-1.21-.79-1.92L13.19 9.75H9.75v1.5h-1.5V9.37c0-.62.5-1.12 1.12-1.12h5.32l2.62-2.62H5.63V15h-1.5V5.63c0-.83.67-1.5 1.5-1.5H18.8l2.63-2.63H2.25Z"></path></svg> Zed </a> </li><li role="presentation"> <a role="tab" href="#tab-panel-139" id="tab-139" aria-selected="false" tabindex="-1"> <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M23.15 2.59 18.2.2a1.5 1.5 0 0 0-1.7.29L7.04 9.13 2.93 6a1 1 0 0 0-1.28.06L.33 7.26a1 1 0 0 0 0 1.48L3.9 12 .32 15.26a1 1 0 0 0 0 1.48l1.33 1.2a1 1 0 0 0 1.28.06l4.12-3.13 9.46 8.63c.44.45 1.13.57 1.7.29l4.94-2.38c.52-.25.85-.77.85-1.35V3.94c0-.58-.33-1.1-.85-1.36ZM18 17.45 10.82 12 18 6.55v10.9Z"></path></svg> VS Code </a> </li> </ul> </div> <div id="tab-panel-138" aria-labelledby="tab-138" role="tabpanel"> <div><figure><figcaption><span>.zed/settings.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"lsp"</span><span>: {</span></div></div><div><div><span> </span><span>"biome"</span><span>: {</span></div></div><div><div><span> </span><span>"settings"</span><span>: {</span></div></div><div><div><span> </span><span>"inline\_config"</span><span>: {</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"suspicious"</span><span>: {</span></div></div><div><div><span> </span><span>"noConsole"</span><span>: </span><span>"</span><span>off</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div> </div> <div id="tab-panel-139" aria-labelledby="tab-139" role="tabpanel" hidden> <div><figure><figcaption><span>.vscode/settings.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"biome.lsp"</span><span>: {</span></div></div><div><div><span> </span><span>"inlineConfig"</span><span>: {</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"suspicious"</span><span>: {</span></div></div><div><div><span> </span><span>"noConsole"</span><span>: </span><span>"</span><span>off</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div> </div> <starlight-tabs-restore></starlight-tabs-restore> </starlight-tabs>
<div><h3 id="major-improvements-to-html-ish-languages">Major improvements to HTML-ish languages</h3></div>
<p>In Biome v2.3, we announced experimental full support for HTML-ish languages such as Vue, Svelte, and Astro. We’ve since focused on improving the developer experience based on community feedback. Several improvements were shipped in patch releases.</p>
<p>Biome 2.4 brings significantly improved parsing for Vue and Svelte, resulting in better formatting across the board. Additionally, the rules <code dir="auto">noUnusedVariables</code>, <code dir="auto">useConst</code>, <code dir="auto">useImportType</code> and <code dir="auto">noUnusedImports</code> have been substantially improved, so you will see fewer false positives.</p>
<p>All these improvements are visible only when the flag <code dir="auto">html.experimentalFullSupportEnabled</code> is set to <code dir="auto">true</code>. If you previously used <a href="https://biomejs.dev/internals/language-support/#linting-html-ish-languages">the <code dir="auto">overrides</code> configuration workaround</a> to disable certain rules, you can now remove it. If you encounter false positives, please report them in this <a href="https://github.com/biomejs/biome/issues/8590">issue</a>. We now have the infrastructure to address these problems.</p>
<p>The CSS parser can now parse Vue SFC syntax such as <code dir="auto">:slotted</code>, <code dir="auto">:deep</code>, and <code dir="auto">v-bind()</code>, as well as <code dir="auto">:global</code> and <code dir="auto">:local</code> inside <code dir="auto">.astro</code>, <code dir="auto">.svelte</code> and <code dir="auto">.vue</code> files.</p>
<div><h3 id="html-accessibility-rules">HTML accessibility rules</h3></div>
<p>Biome 2.4 introduces 15 comprehensive accessibility-focused lint rules for HTML, helping you build more accessible web applications:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-autofocus/"><code dir="auto">noAutofocus</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-positive-tabindex/"><code dir="auto">noPositiveTabindex</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-alt-text/"><code dir="auto">useAltText</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-anchor-content/"><code dir="auto">useAnchorContent</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-media-caption/"><code dir="auto">useMediaCaption</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-html-lang/"><code dir="auto">useHtmlLang</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-valid-lang/"><code dir="auto">useValidLang</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-valid-aria-role/"><code dir="auto">useValidAriaRole</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-aria-props-for-role/"><code dir="auto">useAriaPropsForRole</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-button-type/"><code dir="auto">useButtonType</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-access-key/"><code dir="auto">noAccessKey</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-distracting-elements/"><code dir="auto">noDistractingElements</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-svg-without-title/"><code dir="auto">noSvgWithoutTitle</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-redundant-alt/"><code dir="auto">noRedundantAlt</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-iframe-title/"><code dir="auto">useIframeTitle</code></a></li>
</ul>
<p>These rules work seamlessly with Vue, Svelte, and Astro files. Please help us to ship more <a href="https://github.com/biomejs/biome/issues/8155">a11y rules</a>.</p>
<div><h3 id="rule-profiler">Rule profiler</h3></div>
<p>The commands <code dir="auto">lint</code> and <code dir="auto">check</code> now have a <code dir="auto">--profile-rules</code> flag. This flag enables the new internal profiler, which allows you to capture the execution time of lint rules, assist actions, and GritQL plugins.</p>
<p>The profiler tracks only the execution time of the rule, and it doesn’t track the time spent in querying Biome’s CST. The flag will print an output similar to this one:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>Rule execution time (does not include any preprocessing)</span></div></div><div><div><span><span> </span></span><span>total avg min max count rule</span></div></div><div><div><span><span> </span></span><span>42.069ms 1.010µs 41.000ns 227.625µs 41633 correctness/noUnusedVariables</span></div></div><div><div><span><span> </span></span><span>23.131ms 452.000ns 42.000ns 330.750µs 51096 suspicious/noFocusedTests</span></div></div><div><div><span><span> </span></span><span>9.864ms 193.000ns 0.000ns 149.375µs 51046 suspicious/noConsole</span></div></div><div><div><span><span> </span></span><span>8.074ms 198.000ns 0.000ns 141.208µs 40721 correctness/noUnusedFunctionParameters</span></div></div><div><div><span><span> </span></span><span>7.963ms 137.000ns 0.000ns 263.958µs 57899 style/useNodejsImportProtocol</span></div></div><div><div><span><span> </span></span><span>6.711ms 4.355µs 41.000ns 686.000µs 1541 source/organizeImports</span></div></div><div><div><span><span> </span></span><span>4.076ms 664.000ns 0.000ns 132.792µs 6130 correctness/noUnusedImports</span></div></div><div><div><span><span> </span></span><span>4.015ms 55.000ns 0.000ns 131.250µs 72343 correctness/noTypeOnlyImportAttributes</span></div></div><div><div><span><span> </span></span><span>3.320ms 524.000ns 0.000ns 115.791µs 6334 style/useImportType</span></div></div><div><div><span><span> </span></span><span>384.101µs 164.000ns 0.000ns 74.875µs 2328 correctness/noNodejsModules</span></div></div><div><div><span><span> </span></span><span>384.042µs 2.782µs 42.000ns 163.417µs 138 correctness/noDuplicatePrivateClassMembers</span></div></div><div><div><span><span> </span></span><span>10.753µs 282.000ns 83.000ns 833.000ns 38 correctness/noSuperWithoutExtends</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>One way to interpret the data is to check the rules/actions that have low counts, and check their execution time. For example, if the execution time feels way too high compared to what it should be, maybe it’s a good place to look for possible optimizations. Since we landed this feature, we have found some bottlenecks that we have fixed since then.</p>
<div><h3 id="configuration-file-discovery">Configuration file discovery</h3></div>
<p>Biome 2.4 improves configuration file discovery in two major ways:</p>
<ol>
<li>
<p><strong>Hidden configuration files</strong>: Biome now loads <code dir="auto">.biome.json</code> and <code dir="auto">.biome.jsonc</code> files. The loading order is: <code dir="auto">biome.json</code> → <code dir="auto">biome.jsonc</code> → <code dir="auto">.biome.json</code> → <code dir="auto">.biome.jsonc</code></p>
</li>
<li>
<p><strong>Config home directories</strong>: Biome now attempts to load configuration files from platform-specific config directories:</p>
<ul>
<li><code dir="auto">$XDG\_CONFIG\_HOME</code> or <code dir="auto">$HOME/.config/biome</code> on Linux</li>
<li><code dir="auto">/Users/$USER/Library/Application Support/biome</code> on macOS</li>
<li><code dir="auto">C:\Users\$USER\AppData\Roaming\biome\config</code> on Windows</li>
</ul>
</li>
</ol>
<p>The priority order is: project folder (working directory) → parent folders → config home.</p>
<div><h2 id="linter-and-assist">Linter and Assist</h2></div>
<div><h3 id="new-assist-actions">New Assist Actions</h3></div>
<div><h4 id="remove-duplicate-css-classes">Remove Duplicate CSS Classes</h4></div>
<p>Biome 2.4 introduces the <a href="https://biomejs.dev/assist/actions/no-duplicate-classes/"><code dir="auto">noDuplicateClasses</code></a> assist action to detect and remove duplicate CSS classes.</p>
<p><strong>For JSX files:</strong> Supports <code dir="auto">class</code>, <code dir="auto">className</code> attributes and utility functions like <code dir="auto">clsx</code>, <code dir="auto">cn</code>, <code dir="auto">cva</code>.</p>
<p><strong>For HTML files:</strong> Checks <code dir="auto">class</code> attributes. This is the first assist action for HTML.</p>
<div><figure><figcaption><span>example.jsx</span></figcaption><pre><code><div><div><span>// Before</span></div></div><div><div><span><span>&#x3C;</span><span>div</span><span> </span></span><span>class</span><span>=</span><span>"</span><span>flex p-4 flex</span><span>"</span><span> /></span><span>;</span></div></div><div><div>
</div></div><div><div><span>// After</span></div></div><div><div><span><span>&#x3C;</span><span>div</span><span> </span></span><span>class</span><span>=</span><span>"</span><span>flex p-4</span><span>"</span><span> /></span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Thank you <a href="https://github.com/mldangelo" title="Contributor @mldangelo">
@mldangelo </a> .</p>
<div><h4 id="sort-interface-members">Sort Interface Members</h4></div>
<p>Added a new assist action <code dir="auto">useSortedInterfaceMembers</code> that sorts TypeScript interface members for improved readability. It includes an autofix.</p>
<p>Before:</p>
<div><figure><figcaption><span>example.ts</span></figcaption><pre><code><div><div><span>interface</span><span> MixedMembers {</span></div></div><div><div><span><span> </span></span><span>z</span><span>:</span><span> </span><span>string</span><span>;</span></div></div><div><div><span><span> </span></span><span>a</span><span>:</span><span> </span><span>number</span><span>;</span></div></div><div><div><span> </span><span>()</span><span>:</span><span> </span><span>void</span><span>;</span></div></div><div><div><span><span> </span></span><span>y</span><span>:</span><span> </span><span>boolean</span><span>;</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>After:</p>
<div><figure><figcaption><span>example.ts</span></figcaption><pre><code><div><div><span>interface</span><span> MixedMembers {</span></div></div><div><div><span><span> </span></span><span>a</span><span>:</span><span> </span><span>number</span><span>;</span></div></div><div><div><span><span> </span></span><span>y</span><span>:</span><span> </span><span>boolean</span><span>;</span></div></div><div><div><span><span> </span></span><span>z</span><span>:</span><span> </span><span>string</span><span>;</span></div></div><div><div><span> </span><span>()</span><span>:</span><span> </span><span>void</span><span>;</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="enhanced-lint-rules">Enhanced Lint Rules</h3></div>
<div><h4 id="usesortedkeys-with-groupbynesting-option"><code dir="auto">useSortedKeys</code> with <code dir="auto">groupByNesting</code> Option</h4></div>
<p>Added <code dir="auto">groupByNesting</code> option to the <code dir="auto">useSortedKeys</code> assist. When enabled, object keys are grouped by their value’s nesting depth before sorting alphabetically.</p>
<p>Simple values (primitives, single-line arrays, and single-line objects) are sorted first, followed by nested values (multi-line arrays and multi-line objects).</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"assist"</span><span>: {</span></div></div><div><div><span> </span><span>"actions"</span><span>: {</span></div></div><div><div><span> </span><span>"source"</span><span>: {</span></div></div><div><div><span> </span><span>"useSortedKeys"</span><span>: {</span></div></div><div><div><span> </span><span>"level"</span><span>: </span><span>"</span><span>on</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"options"</span><span>: {</span></div></div><div><div><span> </span><span>"groupByNesting"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="usehookattoplevel-with-ignore-option"><code dir="auto">useHookAtTopLevel</code> with <code dir="auto">ignore</code> Option</h4></div>
<p>Added <code dir="auto">ignore</code> option to the <a href="https://biomejs.dev/linter/rules/use-hook-at-top-level/"><code dir="auto">useHookAtTopLevel</code></a> rule. You can now specify function names that should not be treated as hooks, even if they follow the <code dir="auto">use\*</code> naming convention.</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"correctness"</span><span>: {</span></div></div><div><div><span> </span><span>"useHookAtTopLevel"</span><span>: {</span></div></div><div><div><span> </span><span>"options"</span><span>: {</span></div></div><div><div><span> </span><span>"ignore"</span><span>: [</span><span>"</span><span>useDebounce</span><span>"</span><span>, </span><span>"</span><span>useCustomUtility</span><span>"</span><span>]</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="useiterablecallbackreturn-with-checkforeach-option"><code dir="auto">useIterableCallbackReturn</code> with <code dir="auto">checkForEach</code> Option</h4></div>
<p>The rule <a href="https://biomejs.dev/linter/rules/use-iterable-callback-return/"><code dir="auto">useIterableCallbackReturn</code></a> now supports a <code dir="auto">checkForEach</code> option. When set to <code dir="auto">false</code>, the rule will skip checking for <code dir="auto">forEach()</code> callbacks for returning values.</p>
<div><h4 id="improved-usehookattoplevel-detection">Improved <code dir="auto">useHookAtTopLevel</code> Detection</h4></div>
<p>Updated <a href="https://biomejs.dev/linter/rules/use-hook-at-top-level/"><code dir="auto">useHookAtTopLevel</code></a> to better catch invalid hook usage. The rule now generates diagnostics if:</p>
<ul>
<li>A hook is used at the module level (top of the file, outside any function)</li>
<li>A hook is used within a function or method which is not a hook or component, unless it is a function expression (such as arrow functions commonly used in tests)</li>
</ul>
<div><h4 id="useimportextensions-with-custom-mappings"><code dir="auto">useImportExtensions</code> with Custom Mappings</h4></div>
<p>Added the <code dir="auto">extensionMappings</code> option to <code dir="auto">useImportExtensions</code>. This allows you to specify custom file extensions for different module types. For example, to ban all <code dir="auto">.ts</code> imports in favor of <code dir="auto">.js</code> imports:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"nursery"</span><span>: {</span></div></div><div><div><span> </span><span>"useImportExtensions"</span><span>: {</span></div></div><div><div><span> </span><span>"level"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"options"</span><span>: {</span></div></div><div><div><span> </span><span>"extensionMappings"</span><span>: {</span></div></div><div><div><span> </span><span>"ts"</span><span>: </span><span>"</span><span>js</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="useunifiedtypesignatures-enhancements"><code dir="auto">useUnifiedTypeSignatures</code> Enhancements</h4></div>
<p>Added 2 options from <code dir="auto">typescript-eslint</code> to <a href="https://biomejs.dev/linter/rules/use-unified-type-signatures/"><code dir="auto">useUnifiedTypeSignatures</code></a>:</p>
<ul>
<li><code dir="auto">ignoreDifferentlyNamedParameters</code> - Ignores overload signatures whose parameter names differ</li>
<li><code dir="auto">ignoreDifferentJsDoc</code> - Ignores overload signatures whose JSDoc comments differ</li>
</ul>
<div><h4 id="ignore-options-for-css-rules">Ignore Options for CSS Rules</h4></div>
<p>Added <code dir="auto">ignore</code> option to <a href="https://biomejs.dev/linter/rules/no-unknown-property"><code dir="auto">noUnknownProperty</code></a>, <code dir="auto">noUnknownFunction</code>, <code dir="auto">noUnknownPseudoClass</code>, and <code dir="auto">noUnknownPseudoElement</code>. If an unknown property/function/selector name matches any of the items provided in <code dir="auto">ignore</code>, a diagnostic won’t be emitted.</p>
<div><h4 id="improved-svelte-variables-detection">Improved Svelte Variables Detection</h4></div>
<p>Improved the rule <code dir="auto">noUnusedVariables</code> in Svelte files by correctly detecting variables defined in the JavaScript blocks and used inside the templates.</p>
<div><h3 id="new-linter-domain-types">New Linter Domain: <code dir="auto">types</code></h3></div>
<p>Biome 2.4 introduces a new linter domain called <code dir="auto">types</code>. This domain enables all rules that require the type inference engine to function.</p>
<p>As opposed to the <code dir="auto">project</code> domain (which only enables rules that require the module graph), the <code dir="auto">types</code> domain specifically targets rules that need type information.</p>
<p>The following nursery rules have been moved to the <code dir="auto">types</code> domain:</p>
<ul>
<li><code dir="auto">useArraySortCompare</code></li>
<li><code dir="auto">useAwaitThenable</code></li>
<li><code dir="auto">useFind</code></li>
<li><code dir="auto">useRegexpExec</code></li>
<li><code dir="auto">noUnnecessaryConditions</code></li>
<li><code dir="auto">noMisusedPromises</code></li>
<li><code dir="auto">noFloatingPromises</code></li>
</ul>
<p>This allows you to enable or disable type-based linting more granularly using the <code dir="auto">--only</code> and <code dir="auto">--skip</code> flags.</p>
<div><h3 id="promoted-rules">Promoted Rules</h3></div>
<p>Biome 2.4 promotes 24 nursery rules to stable groups, making them production-ready.</p>
<div><h4 id="correctness-rules">Correctness Rules</h4></div>
<p>Promoted the following rules to the <code dir="auto">correctness</code> group:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-unresolved-imports/"><code dir="auto">noUnresolvedImports</code></a> - Reports imports that cannot be resolved</li>
<li><a href="https://biomejs.dev/linter/rules/no-vue-reserved-props/"><code dir="auto">noVueReservedProps</code></a> - Reports Vue reserved props usage</li>
<li><a href="https://biomejs.dev/linter/rules/no-vue-reserved-keys/"><code dir="auto">noVueReservedKeys</code></a> - Reports Vue reserved keys usage</li>
<li><a href="https://biomejs.dev/linter/rules/no-vue-data-object-declaration/"><code dir="auto">noVueDataObjectDeclaration</code></a> - Reports Vue 2 data declared as an object instead of a function</li>
<li><a href="https://biomejs.dev/linter/rules/no-next-async-client-component/"><code dir="auto">noNextAsyncClientComponent</code></a> - Reports async Next.js client components</li>
<li><a href="https://biomejs.dev/linter/rules/no-vue-duplicate-keys/"><code dir="auto">noVueDuplicateKeys</code></a> - Reports duplicate keys in Vue component options</li>
<li><a href="https://biomejs.dev/linter/rules/no-vue-setup-props-reactivity-loss/"><code dir="auto">noVueSetupPropsReactivityLoss</code></a> - Reports destructuring of props in Vue 3 setup which causes reactivity loss</li>
<li><a href="https://biomejs.dev/linter/rules/use-qwik-method-usage/"><code dir="auto">useQwikMethodUsage</code></a> - Enforces correct Qwik framework method usage</li>
<li><a href="https://biomejs.dev/linter/rules/use-qwik-valid-lexical-scope/"><code dir="auto">useQwikValidLexicalScope</code></a> - Enforces valid lexical scope in Qwik framework</li>
</ul>
<div><h4 id="suspicious-rules">Suspicious Rules</h4></div>
<p>Promoted the following rules to the <code dir="auto">suspicious</code> group:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-import-cycles/"><code dir="auto">noImportCycles</code></a> - Reports circular imports</li>
<li><a href="https://biomejs.dev/linter/rules/no-deprecated-imports/"><code dir="auto">noDeprecatedImports</code></a> - Reports imports of deprecated symbols</li>
<li><a href="https://biomejs.dev/linter/rules/no-react-forward-ref/"><code dir="auto">noReactForwardRef</code></a> - Reports usage of <code dir="auto">React.forwardRef</code></li>
<li><a href="https://biomejs.dev/linter/rules/no-unused-expressions/"><code dir="auto">noUnusedExpressions</code></a> - Reports expressions that are never used</li>
<li><a href="https://biomejs.dev/linter/rules/no-empty-source/"><code dir="auto">noEmptySource</code></a> - Reports empty source files</li>
<li><a href="https://biomejs.dev/linter/rules/use-deprecated-date/"><code dir="auto">useDeprecatedDate</code></a> - Enforces use of GraphQL <code dir="auto">@deprecated</code> directive with date</li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-dependencies/"><code dir="auto">noDuplicateDependencies</code></a> - Reports duplicate dependencies in package.json</li>
</ul>
<div><h4 id="complexity-rules">Complexity Rules</h4></div>
<p>Promoted the following rules to the <code dir="auto">complexity</code> group:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-useless-undefined/"><code dir="auto">noUselessUndefined</code></a> - Reports useless <code dir="auto">undefined</code> initialization and returns</li>
<li><a href="https://biomejs.dev/linter/rules/use-max-params/"><code dir="auto">useMaxParams</code></a> - Enforces a maximum number of function parameters</li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-catch-binding/"><code dir="auto">noUselessCatchBinding</code></a> - Reports useless catch binding parameters</li>
</ul>
<div><h4 id="style-rules">Style Rules</h4></div>
<p>Promoted the following rules to the <code dir="auto">style</code> group:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/use-consistent-arrow-return/"><code dir="auto">useConsistentArrowReturn</code></a> - Enforces consistent return in arrow functions</li>
<li><a href="https://biomejs.dev/linter/rules/no-jsx-literals/"><code dir="auto">noJsxLiterals</code></a> - Reports literal strings in JSX</li>
</ul>
<div><h2 id="formatter">Formatter</h2></div>
<div><h3 id="embedded-snippets-formatting">Embedded Snippets Formatting</h3></div>
<p>Biome 2.4 can now format embedded CSS and GraphQL snippets within JavaScript files. See the <a href="#embedded-snippets-in-javascript">Embedded snippets in JavaScript</a> section in Highlights for details and examples.</p>
<div><h3 id="trailing-newline-option">Trailing Newline Option</h3></div>
<p>Added the formatter option <a href="https://biomejs.dev/reference/configuration/#formattertrailingnewline"><code dir="auto">trailingNewline</code></a>. When set to <code dir="auto">false</code>, the formatter will remove the trailing newline at the end of formatted files. The default value is <code dir="auto">true</code>, which preserves the current behavior.</p>
<p>This option is available globally and for each language-specific formatter configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"trailingNewline"</span><span>: </span><span>false</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"trailingNewline"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>CLI flags are also available: <code dir="auto">--formatter-trailing-newline</code>, <code dir="auto">--javascript-formatter-trailing-newline</code>, <code dir="auto">--json-formatter-trailing-newline</code>, etc.</p>
<aside aria-label="Caution"><p aria-hidden="true">Caution</p><div><p>Setting <code dir="auto">trailingNewline</code> to <code dir="auto">false</code> can cause issues in certain environments and tools. Many POSIX-compliant tools and text editors expect files to end with a newline character. Removing the trailing newline may result in:</p><ul>
<li>Warnings or errors from compilers and interpreters</li>
<li>Issues with shell scripts that may not process the last line correctly</li>
<li>Problems with version control systems showing unnecessary diff changes</li>
<li>Incompatibility with coding standards that require POSIX-compliant text files</li>
</ul><p>We recommend keeping the default value of <code dir="auto">true</code> unless you have a specific requirement to remove trailing newlines.</p></div></aside>
<div><h3 id="top-level-suppression-comments">Top-Level Suppression Comments</h3></div>
<p>Added support for the top-level suppression comment <code dir="auto">biome-ignore-all format: &#x3C;explanation></code>. When placed at the beginning of the document, Biome won’t format the code.</p>
<div><figure><figcaption><span>generated.js</span></figcaption><pre><code><div><div><span>// biome-ignore-all format: generated</span></div></div><div><div>
</div></div><div><div><span>const </span><span>a</span><span> =</span><span> [];</span></div></div><div><div><span>const </span><span>b</span><span> =</span><span> [];</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="formatting-applied-with-code-fixes">Formatting Applied with Code Fixes</h3></div>
<p>Formatting is now applied when applying safe/unsafe fixes via <code dir="auto">biome check</code>. This ensures your code is properly formatted after applying automated fixes.</p>
<div><h3 id="css-parser-improvements">CSS Parser Improvements</h3></div>
<div><h4 id="css-function-at-rule-support">CSS <code dir="auto">@function</code> At-Rule Support</h4></div>
<p>Added support for parsing and formatting the CSS <code dir="auto">@function</code> at-rule from the <a href="https://drafts.csswg.org/css-mixins-1/#function-rule">CSS Mixins Module Level 1</a> specification:</p>
<div><figure><figcaption><span>styles.css</span></figcaption><pre><code><div><div><span>@function</span><span> --transparent(--color &#x3C;color>, --alpha &#x3C;number>: 0.5) returns &#x3C;color> {</span></div></div><div><div><span> </span><span>result: oklch(from var(--color</span><span>) </span><span>l c h</span><span> / </span><span>var(--alpha</span><span>));</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="css-modules-auto-detection">CSS Modules Auto-Detection</h4></div>
<p>Biome now automatically enables CSS modules parsing for <code dir="auto">\*.module.css</code> files. If your codebase only uses <code dir="auto">\*.module.css</code> files, you can remove the manual parser configuration.</p>
<div><h4 id="css-properties-ordering-update">CSS Properties Ordering Update</h4></div>
<p>Updated the CSS properties ordering to align with <code dir="auto">stylelint-config-recess-order</code> v7.4.0, adding support for containment properties, font synthesis properties, ruby properties, color adjustment properties, view transitions properties, shapes properties, motion path properties, and more.</p>
<div><h4 id="css-module-syntax-in-vuesvelteastro">CSS Module Syntax in Vue/Svelte/Astro</h4></div>
<p>Added support for parsing <code dir="auto">:global</code> and <code dir="auto">:local</code> inside <code dir="auto">.astro</code>, <code dir="auto">.svelte</code> and <code dir="auto">.vue</code> files, in the <code dir="auto">&#x3C;style></code> portion of the file. This capability is only available when <code dir="auto">experimentalFullHtmlSupportEnabled</code> is set to <code dir="auto">true</code>.</p>
<div><h2 id="cli">CLI</h2></div>
<div><h3 id="enhanced---skip-and---only-flags">Enhanced <code dir="auto">--skip</code> and <code dir="auto">--only</code> Flags</h3></div>
<p>Added <code dir="auto">--only</code> and <code dir="auto">--skip</code> options to <code dir="auto">biome check</code> and <code dir="auto">biome ci</code>, covering both lint diagnostics and assist actions. You can now run or exclude specific:</p>
<ul>
<li>Lint rules</li>
<li>Assist actions</li>
<li>Groups of rules and actions</li>
<li>Domains (including the new <code dir="auto">types</code> domain)</li>
</ul>
<p>Examples:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>check</span><span> </span><span>--only=suspicious/noDebugger</span><span> </span><span>src/</span><span>\*\*</span><span>/</span><span>\*</span><span>.js</span></div></div><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--skip=project</span><span> </span><span>src/</span><span>\*\*</span></div></div><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--only=types</span><span> </span><span># Run only type-based rules</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="multiple-reporters-and-reporter-output-to-files">Multiple Reporters and Reporter Output to Files</h3></div>
<p>Biome 2.4 adds support for multiple reporters and the ability to save reporter output to arbitrary files.</p>
<div><h4 id="combine-multiple-reporters-in-ci">Combine Multiple Reporters in CI</h4></div>
<p>If you run Biome on GitHub, you can now use both the default reporter and the GitHub reporter:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--reporter=default</span><span> </span><span>--reporter=github</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="save-reporter-output-to-a-file">Save Reporter Output to a File</h4></div>
<p>With the new <code dir="auto">--reporter-file</code> CLI option, it’s now possible to save the output of all reporters to a file:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--reporter=rdjson</span><span> </span><span>--reporter-file=/etc/tmp/report.json</span></div></div><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--reporter=summary</span><span> </span><span>--reporter-file=./reports/file.txt</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>You can combine these two features. For example, have the <code dir="auto">default</code> reporter written on terminal, and the <code dir="auto">rdjson</code> reporter written on file:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--reporter=default</span><span> </span><span>--reporter=rdjson</span><span> </span><span>--reporter-file=/etc/tmp/report.json</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p><strong>The <code dir="auto">--reporter</code> and <code dir="auto">--reporter-file</code> flags must appear next to each other.</strong></p>
<div><h3 id="new-sarif-reporter">New SARIF Reporter</h3></div>
<p>Added a new reporter <code dir="auto">--reporter=sarif</code>, that emits diagnostics using the <a href="https://sarifweb.azurewebsites.net/">SARIF</a> format. This is particularly useful for integrating Biome with security and code quality platforms.</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>ci</span><span> </span><span>--reporter=sarif</span><span> </span><span>--reporter-file=biome-results.sarif</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="file-watcher-control">File Watcher Control</h3></div>
<p>Added new CLI options to the commands <code dir="auto">lsp-proxy</code> and <code dir="auto">start</code> that allow control over the Biome file watcher:</p>
<ul>
<li><strong><code dir="auto">--watcher-kind</code></strong> (env: <code dir="auto">BIOME\_WATCHER\_KIND</code>): Controls how the Biome file watcher behaves. Options: <code dir="auto">recommended</code> (default), <code dir="auto">polling</code>, or <code dir="auto">none</code>.</li>
<li><strong><code dir="auto">--watcher-polling-interval</code></strong> (env: <code dir="auto">BIOME\_WATCHER\_POLLING\_INTERVAL</code>): The polling interval in milliseconds when using <code dir="auto">polling</code> mode (defaults to 2000ms).</li>
</ul>
<div><h3 id="enhanced-logging-options">Enhanced Logging Options</h3></div>
<p>Revamped the logging options for all Biome commands. The commands <code dir="auto">format</code>, <code dir="auto">lint</code>, <code dir="auto">check</code>, <code dir="auto">ci</code>, <code dir="auto">search</code>, <code dir="auto">lsp-proxy</code> and <code dir="auto">start</code> now accept consistent logging CLI options with environment variable aliases:</p>
<ul>
<li><code dir="auto">--log-file</code> (env: <code dir="auto">BIOME\_LOG\_FILE</code>) - Optional path/file to redirect log messages to</li>
<li><code dir="auto">--log-prefix-name</code> (env: <code dir="auto">BIOME\_LOG\_PREFIX\_NAME</code>) - Allows changing the prefix applied to the file name of the logs (daemon only)</li>
<li><code dir="auto">--log-path</code> (env: <code dir="auto">BIOME\_LOG\_PATH</code>) - Allows changing the folder where logs are stored (daemon only)</li>
<li><code dir="auto">--log-level</code> (env: <code dir="auto">BIOME\_LOG\_LEVEL</code>) - The level of logging: <code dir="auto">debug</code>, <code dir="auto">info</code>, <code dir="auto">warn</code>, <code dir="auto">error</code>, or <code dir="auto">none</code></li>
<li><code dir="auto">--log-kind</code> (env: <code dir="auto">BIOME\_LOG\_KIND</code>) - What the log should look like</li>
</ul>
<div><h3 id="stacktrace-for-fatal-errors">Stacktrace for Fatal Errors</h3></div>
<p>It’s now possible to provide the stacktrace for a fatal error. The stacktrace is only available when the environment variable <code dir="auto">RUST\_BACKTRACE=1</code> is set:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>RUST\_BACKTRACE</span><span>=</span><span>1</span><span> </span><span>biome</span><span> </span><span>lint</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="additional-features">Additional Features</h2></div>
<div><h3 id="gritql-json-support">GritQL JSON Support</h3></div>
<p>Added JSON as a target language for GritQL pattern matching. You can now write Grit plugins for JSON files, enabling:</p>
<ul>
<li>Searching and transforming JSON configuration files</li>
<li>Enforcing patterns in <code dir="auto">package.json</code> and other JSON configs</li>
<li>Writing custom lint rules for JSON using GritQL</li>
</ul>
<p>Example patterns:</p>
<p>Match all key-value pairs:</p>
<div><figure><figcaption><span>pattern.grit</span></figcaption><pre><code><div><div><span>language json</span></div></div><div><div><span>pair(key = $k, value = $v)</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Match objects with specific structure:</p>
<div><figure><figcaption><span>pattern.grit</span></figcaption><pre><code><div><div><span>language json</span></div></div><div><div><span>JsonObjectValue()</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Supports both native Biome AST names (<code dir="auto">JsonMember</code>, <code dir="auto">JsonObjectValue</code>) and TreeSitter-compatible names (<code dir="auto">pair</code>, <code dir="auto">object</code>, <code dir="auto">array</code>) for compatibility with existing Grit patterns.</p>
<p>For more details, see the <a href="https://biomejs.dev/reference/gritql/">GritQL documentation</a>.</p>
<div><h3 id="lsp-and-editor-features">LSP and Editor Features</h3></div>
<div><h4 id="lsp-progress-reporting">LSP Progress Reporting</h4></div>
<p>The Biome Language Server now reports progress while scanning files and dependencies in the project, providing better feedback during long-running operations.</p>
<div><h3 id="configuration-and-editor-support">Configuration and Editor Support</h3></div>
<div><h4 id="cursor-files-support">Cursor Files Support</h4></div>
<p>Added support for Cursor files. When Biome sees a Cursor JSON file, it will parse it with comments enabled and trailing commas enabled:</p>
<ul>
<li><code dir="auto">$PROJECT/.cursor/</code></li>
<li><code dir="auto">%APPDATA%\Cursor\User\</code> on Windows</li>
<li><code dir="auto">~/Library/Application Support/Cursor/User/</code> on macOS</li>
<li><code dir="auto">~/.config/Cursor/User/</code> on Linux</li>
</ul>
<div><h3 id="other-improvements">Other Improvements</h3></div>
<div><h4 id="vue-sfc-css-syntax-support">Vue SFC CSS Syntax Support</h4></div>
<p>The Biome CSS parser is now able to parse Vue SFC syntax such as <code dir="auto">:slotted</code>, <code dir="auto">:deep</code>, and <code dir="auto">v-bind()</code>. These pseudo-functions and directives are only correctly parsed when the CSS is defined inside <code dir="auto">.vue</code> components.</p>
<p>This capability is only available when <code dir="auto">experimentalFullHtmlSupportEnabled</code> is set to <code dir="auto">true</code>.</p>
<div><h4 id="e18e-eslint-plugin-support">e18e ESLint Plugin Support</h4></div>
<p>Added e18e ESLint plugin as a recognized rule source. Six Biome rules now reference their e18e equivalents: <code dir="auto">useAtIndex</code>, <code dir="auto">useExponentiationOperator</code>, <code dir="auto">noPrototypeBuiltins</code>, <code dir="auto">useDateNow</code>, <code dir="auto">useSpread</code>, and <code dir="auto">useObjectSpread</code>.</p>
<div><h2 id="more-improvements">More Improvements</h2></div>
<p>In addition to the features highlighted above, Biome 2.4 includes numerous bug fixes, performance improvements, and smaller enhancements across the toolchain. For a complete list of changes, refer to the <a href="https://biomejs.dev/internals/changelog/version/2-4-0/">changelog page</a>.</p>
<div><h2 id="i-like-where-this-is-going-how-can-i-help">I like where this is going, how can I help?</h2></div>
<p>I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome.</p>
<div><h3 id="translations">Translations</h3></div>
<p>If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this <a href="https://biomejs.dev/i18n-dashboard/">dashboard</a>, you can check the supported languages and if they are up-to-date.</p>
<div><h3 id="chat-with-us">Chat with us</h3></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. Chatting with the community and being part of the community is a form of contribution.</p>
<div><h3 id="code-contributions">Code contributions</h3></div>
<p>If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project for you!</p>
<p>There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:</p>
<ul>
<li>Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very <a href="https://github.com/biomejs/biome/blob/main/crates/biome\_analyze/CONTRIBUTING.md">extensive technical guide</a>.</li>
<li><a href="https://github.com/biomejs/biome/blob/main/crates/biome\_parser/CONTRIBUTING.md">Help</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_yaml\_parser">building</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_html\_parser">Biome</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_markdown\_parser">parsers</a>!
One interesting fact about Biome parsers is that they are recoverable parsers <a href="https://biomejs.dev/internals/architecture/#parser-and-cst">error resilient</a> which emit a <a href="https://en.wikipedia.org/wiki/Parse\_tree">CST</a> instead of a classic AST.</li>
<li>Implement new capabilities in our <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_lsp">LSP (Language Server Protocol)</a>, or add new features in one of our editor extensions: <a href="https://github.com/biomejs/biome-vscode">VS Code</a>, <a href="https://github.com/biomejs/biome-zed">Zed</a> and <a href="https://github.com/biomejs/biome-intellij">JetBrains IntelliJ</a>.</li>
</ul>
<div><h3 id="financial-help">Financial help</h3></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program </a> where you as a company can employ one of the core contributors to work a specific aspect of the Biome toolchain.</p>Roadmap 2026https://biomejs.dev/blog/roadmap-2026/https://biomejs.dev/blog/roadmap-2026/What to expect from Biome in 2026, and what Biome has achieved in 2025.
Wed, 21 Jan 2026 00:00:00 GMT<p><strong>In this article, we want to share with you all our roadmap for 2026!</strong></p>
<p>The roadmap is a collection of ideas and interests that the maintainers of the project collect from various sources: user’s feedback, personal interests, time available to dedicate to the project, user’s proposal from GitHub discussions.</p>
<p>The roadmap represents the overall direction that we want to take; however, things can change overtime.</p>
<div><h2 id="2025-achievements">2025 achievements</h2></div>
<ul>
<li>We shipped Biome v2, which brought amazing new features to the ecosystem:
<ul>
<li>Support for nested configuration files, and better support in monorepos.</li>
<li>First tool to ship type-aware lint rules that don’t rely on the TypeScript compiler (commonly known as <code dir="auto">tsc</code>), thanks to its inference engine, <a href="https://biomejs.dev/blog/vercel-partners-biome-type-inference/">sponsored by Vercel</a>.</li>
<li>Support for project lint rules, such as <a href="https://biomejs.dev/linter/rules/no-import-cycles/"><code dir="auto">noImportCycle</code></a>.</li>
<li>Shipped the new concept of <a href="https://biomejs.dev/linter/domains">linter domains</a>, a way to group different rules under different umbrellas, and a way to turn on those rules automatically based on your dependencies.</li>
<li>Added support for plugins via <a href="https://docs.grit.io/">GritQL</a>. Throughout the year the plugin engine has become even more powerful, allowing users to <strong>query the Biome CST</strong> and report custom diagnostics.</li>
<li>Shipped the new <a href="https://biomejs.dev/assist/actions/organize-imports/">JavaScript import and export organizer</a> that provides advanced features like import merging, and custom import groups.</li>
</ul>
</li>
<li>We shipped <strong>three new minors</strong> after v2, which have added many new features:
<ul>
<li>Support for Tailwind syntax in CSS files</li>
<li>Experimental full support of parsing, formatting, linting for Vue, Svelte, and Astro. The language capabilities of Biome have improved and allow them to inspect multiple languages in the same document.</li>
<li>We improved and fixed many bugs around the Biome watcher and scanner. Some of those bugs caused some memory leaks, causing Biome to be unusable for some users.</li>
</ul>
</li>
<li>We have surpassed <a href="https://www.npmcharts.com/compare/@biomejs/biome?interval=30">15 million monthly downloads</a>.</li>
<li>GritQL has now become part of the <a href="https://biomejs.dev/blog/gritql-under-biome-umbrella/">Biome</a> <a href="https://github.com/biomejs/gritql">organization</a>.</li>
</ul>
<div><h3 id="past-mistakes">Past mistakes</h3></div>
<p>Of course, Biome and team are far from being perfect, so we want to acknowledge some of our past mistakes that we hope to address this year. We want to address them moving forward.</p>
<div><h4 id="monorepo-out-of-the-box">Monorepo out of the box</h4></div>
<p>Biome is able to discover nested ignore files and nested configuration files out of the box, without any particular configuration. While this provides an optimal DX, it uncovered some undesired situations where memory leaks get out of hand. Also, in some cases, users don’t have enough control over the folders that are real libraries.</p>
<div><h4 id="difficult-to-debug">Difficult to debug</h4></div>
<p>With so many features, we overlooked the debugging capabilities of the tool. With the rise of tools such as <code dir="auto">ultracite</code>, big monorepos, <code dir="auto">overrides</code>, <code dir="auto">extends</code>, and more, it has become difficult to understand and debug a complex configuration file. This is frustrating for both maintainers and users.</p>
<div><h4 id="poor-communication">Poor communication</h4></div>
<p>Later last year, we announced the experimental full support of Vue, Svelte, and Astro. Many users weren’t happy about how we framed the announcement, especially after some users rightfully complained about the poor support of the Svelte files.</p>
<div><h2 id="2026-roadmap">2026 roadmap</h2></div>
<p>I can’t stress enough that Biome is a community-driven project, all the features we want to implement are driven by our passions and needs. We can’t promise that all of these features will be implemented. Alas, we will try our best to stay aligned and deliver what’s listed below.</p>
<ul>
<li>
<p><strong>JavaScript embedded languages</strong>: improve the DX of the embedded languages in JavaScript, such as CSS and GraphQL.</p>
</li>
<li>
<p><strong>Stabilize everything around HTML</strong></p>
<ul>
<li>Improve HTML formatting so that its formatting matches Prettier’s as much as possible.</li>
<li>Enhance existing lint rules so that they work for HTML-ish languages too, notably Vue, Svelte, and Astro</li>
</ul>
</li>
<li>
<p><strong>Cross-language lint rules</strong>: we want to explore and deliver lint rules that work across languages. Now that Biome has the infrastructure to do so, we might be able to achieve it. What’s a cross-language lint rule, you ask? Here’s an example: have you ever discovered a CSS class not used anywhere? What if there was a lint rule able to discover all your CSS styles, and check if they are actually used inside JSX/HTML-ish files? That’s where a cross-language lint rule comes into play!</p>
</li>
<li>
<p><strong>Opt-in, improved <code dir="auto">workspaces</code></strong>: this is mostly an idea, but we want to address the <a href="#monorepo-out-of-the-box">poor DX introduced by monorepo-out-the-box</a>, by making it opt-in and offer better control. For example, we envision a solution where the configuration might look like this:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"workspaces"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>packages/\*</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"</span><span>utilities/\*</span><span>"</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>With a configuration like this, Biome knows where to look for possible nested configuration files. We believe a solution like this <strong>might improve the DX and the performance of the tool</strong>.</p>
</li>
<li>
<p><strong>SCSS support</strong>: we want to ship SCSS support. It was our <a href="https://github.com/biomejs/biome/discussions/3441">most wanted</a>. We recently closed it, and started the works.</p>
</li>
<li>
<p><strong>More lint rules and assist actions</strong>: keep shipping new lint rules, and assist actions. We recently started implementing <a href="https://github.com/biomejs/biome/issues/8155">Accessibility lint rules for HTML-ish languages</a>.</p>
</li>
<li>
<p><strong>Improve LSP features</strong>: we want to explore and ship more LSP features. Internally, Biome has a module graph that can analyze and link with each other different files, such as JavaScript, CSS, and more. We want to explore and ship more IDE capabilities, such as the ability to highlight a reference such as a CSS class inside a JSX snippet, and allow users to navigate to its declaration inside the CSS file with a click.</p>
</li>
<li>
<p><strong>Stabilize YAML</strong>: our YAML parser is almost ready! Once the parsing is stable enough, formatting is just right there.</p>
</li>
</ul>
<div><h3 id="markdown">Markdown</h3></div>
<p>We really wish to implement the parsing of Markdown; however, we don’t have enough time and resources to look into it. If there’s someone who wishes to help, please let us know on <a href="https://biomejs.dev/chat">Discord</a>! We’re looking for <strong>a champion</strong> who would help with the implementation <strong>and the reviews</strong>.</p>
<div><h2 id="can-i-help-move-biomes-roadmap-forward">Can I help move Biome’s roadmap forward?</h2></div>
<p>We’re glad you asked! Biome is a project led by volunteers who like programming, open-source, and who embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h3 id="chat-with-us">Chat with us</h3></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. You may always ask around if there’s something you can help with.</p>
<p>We also have a <a href="https://github.com/biomejs/biome/issues/2463">GitHub umbrella issue</a> that you can check out, but please be cautious to not start any work until you’ve engaged with the community first. This way we can be mindful of your contributions too.</p>
<div><h3 id="financial-help">Financial help</h3></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program</a> that companies can use to contract a core contributor to work on a specific aspect of the Biome toolchain.</p>GritQL accepted by the Biome organisationhttps://biomejs.dev/blog/gritql-under-biome-umbrella/https://biomejs.dev/blog/gritql-under-biome-umbrella/GritQL has been in use by Biome as our preferred plugin language for a while now. As of today, we are happy to announce that GritQL comes under the Biome umbrella.
Thu, 18 Dec 2025 00:00:00 GMT<p>Today, we are happy and grateful to make a special announcement regarding the continuation of <a href="https://docs.grit.io/">GritQL</a>.</p>
<p>Some observant members of the Biome and GritQL communities may have already spotted that something big was happening behind the scenes: Biome is now the proud owner of the <a href="https://github.com/orgs/biomejs/repositories?q=gritql">GritQL repositories</a>.</p>
<p>Ever since Biome 2.0, GritQL plugins have been supported as a mechanism to add custom linter rules to your project. We took a big gamble here, as GritQL was being pioneered by a startup led by <a href="https://github.com/morgante">Morgante Pell</a> and the future of the language was still uncertain.</p>
<p>We took a leap of faith, because we believed in Morgante’s vision of how GritQL can make plugin writing more intuitive for our end users. The expressive power of GritQL makes it so that end users can intuitively understand how to write plugins, even if they’re not familiar with the internals of AST structures themselves.</p>
<div><h2 id="so-does-that-mean-biome-is-now-responsible-for-the-development-of-gritql">So, does that mean Biome is now responsible for the development of GritQL?</h2></div>
<p>Yes, it does.</p>
<p>But Morgante’s gift came with something even more precious: he personally joined the Biome maintainers team. From under the Biome umbrella, he can continue working on GritQL and our plugin infrastructure as he sees fit.</p>
<p>Please keep in mind that all Biome maintainers are volunteers, as most of us work on Biome in our free time. We have a respectful community that understands this, and this is something we continue to treasure.</p>
<div><h2 id="what-does-this-mean-for-biomes-plugin-infrastructure-concretely">What does this mean for Biome’s plugin infrastructure, concretely?</h2></div>
<p>It’s hard to say exactly.</p>
<p>Early 2024, we drafted our initial <a href="https://github.com/biomejs/biome/discussions/1762">Plugin Proposal RFC</a>. The release of Biome 2.0 in June 2025 saw the first realisation of Biome’s vision in the form of GritQL linter plugins. That leaves a lot of work on the table still, but as usual we’ll keep you posted.</p>
<div><h2 id="where-does-this-leave-javascripttypescript-plugins">Where does this leave JavaScript/TypeScript plugins?</h2></div>
<p>We do recognise that not everyone likes writing plugins using GritQL.</p>
<p>As the RFC mentioned, we also intend to work towards support for JS/TS plugins too. This August, we <a href="https://github.com/biomejs/biome/pull/7300">integrated</a> <a href="https://boajs.dev/">Boa</a> as a JavaScript interpreter that we can integrate into Biome. Back in 2024, Morgante also proposed a <a href="https://github.com/biomejs/gritql/discussions/403">TypeScript API</a> for GritQL so that users may or may not be able to use both forms of plugin functionality together. We don’t know how this will pan out yet, but hopefully with Morgante’s commitment, some of the work may speed up a bit.</p>
<div><h2 id="can-i-help-move-biomes-plugin-efforts-forward">Can I help move Biome’s plugin efforts forward?</h2></div>
<p>We’re glad you asked! Biome is a project led by volunteers who like programming, open-source, and who embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h3 id="chat-with-us">Chat with us</h3></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. We have a dedicated <code dir="auto">#plugins</code> channel that can be used for this purpose. You may always ask around if there’s something you can help with.</p>
<p>We also have a <a href="https://github.com/biomejs/biome/issues/2463">GitHub umbrella issue</a> that you can check out, but please be cautious to not start any work until you’ve engaged with the community first. This way we can be mindful of your contributions too.</p>
<div><h3 id="financial-help">Financial help</h3></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program</a> that companies can use to contract a core contributor to work on a specific aspect of the Biome toolchain.</p>
<div><h2 id="acknowledgements">Acknowledgements</h2></div>
<div><h2 id="biome-by-the-numbers">Biome by the numbers</h2></div>
<p>Biome is a <strong>big Rust project</strong>, that keeps growing over time. As of 17 November (time of writing of the blog post), the project has the following stats:</p>
<ul>
<li>A total of 90 internal crates (AKA <code dir="auto">biome\_\*</code> crates) that are compiled and shipped in production.</li>
<li>~651,971 lines of code between production code and test code.</li>
<li>~3,217 Rust files, between production code and test code.</li>
</ul>
<p>Since Rust is a compiled language, with complex syntax, the resources required for compilation, testing, etc. are bound to increase over time. Before Depot came to the rescue, Biome used to use GitHub Action runners. Here’s a few numbers:</p>
<ul>
<li>Linting for pull requests took around ~15 minutes.</li>
<li>Tests for pull requests took around ~20 minutes.</li>
<li>Benchmarks for pull requests took around ~30 minutes. Benchmarks take longer because the code is compiled in production mode, and we make sure to stress test
our infrastructure by feeding the benchmarks very complex inputs.</li>
<li>A release might have required up to ~45 minutes.</li>
<li>At some point, Biome on Windows couldn’t compile due to the memory required, which exceeded the memory available in the GitHub Actions runners.</li>
</ul>
<div><h2 id="enter-depot">Enter Depot</h2></div>
<table><thead><tr><th>Workflow</th><th>Before (GitHub runners)</th><th>After (Depot)</th></tr></thead><tbody><tr><td>Linting</td><td>~15 minutes</td><td>~2 minutes</td></tr><tr><td>Tests</td><td>~20 minutes</td><td>~4 minutes</td></tr><tr><td>Benchmarks</td><td>~30 minutes</td><td>~15 minutes</td></tr><tr><td>Releases</td><td>~45 minutes</td><td>~25 minutes</td></tr></tbody></table>
<div><h2 id="depots-impact-on-the-ecosystem">Depot’s impact on the ecosystem</h2></div>
<p>These aren’t just numbers. Having a faster CI has had a significant <strong>positive impact</strong> to maintainers, contributors and end-users.</p>
<div><h3 id="maintainers">Maintainers</h3></div>
<p>We’ve seen positive outcomes throughout the entire project management process. We’re able to get faster feedback from our CI jobs, release more frequently and with more confidence, and we can fix CI issues faster. As you know, CI is a <a href="https://www.urbandictionary.com/define.php?term=Yolo">YOLO</a> practice!</p>
<div><h3 id="contributors">Contributors</h3></div>
<p>Contributors can see the effect of their PRs way faster than before, and they can fix possible bugs promptly. This means that by the time a maintainer comes and reviews the PR, it might be approved already because the CI is green! One reason why we’re able to ship so many fixes in every patch release.</p>
<div><h3 id="end-users">End-users</h3></div>
<p>End-users - you, the developers - can enjoy that fix you needed sooner than before!</p>
<div><h2 id="depots-endorsement">Depot’s endorsement</h2></div>
<p>As Vercel did before, Depot believes that <a href="https://biomejs.dev/blog/vercel-partners-biome-type-inference/">Biome’s inference engine</a> can and will improve the developer experience even further.</p>
<p>Depot believes in Biome’s mission, a unified toolchain where users can think less about their tools and dependencies, and more about building their own software using modern practices.</p>
<p><strong>Thank you, Depot!</strong></p>
<div><h2 id="i-like-where-this-is-going-how-can-i-help">I like where this is going, how can I help?</h2></div>
<p>I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h4 id="translations">Translations</h4></div>
<p>If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this <a href="https://biomejs.dev/i18n-dashboard/">dashboard</a>, you can check the supported languages and if they are up to date.</p>
<div><h4 id="chat-with-us">Chat with us</h4></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. Chatting with the community and being part of the community is a form of contribution.</p>
<div><h4 id="code-contributions">Code contributions</h4></div>
<p>If you like the technical aspects of the project, and you want to make your way into the Rust language, or you wish to practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!</p>
<p>There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:</p>
<ul>
<li>Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very <a href="https://github.com/biomejs/biome/blob/main/crates/biome\_analyze/CONTRIBUTING.md">extensive technical guide</a>.</li>
<li><a href="https://github.com/biomejs/biome/blob/main/crates/biome\_parser/CONTRIBUTING.md">Help</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_yaml\_parser">building</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_html\_parser">Biome</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_markdown\_parser">parsers</a>!
One interesting fact about Biome parsers is that they are recoverable parsers <a href="https://biomejs.dev/internals/architecture/#parser-and-cst">error resilient</a> which emit a <a href="https://en.wikipedia.org/wiki/Parse\_tree">CST</a> instead of a classic AST.</li>
<li>Implement new capabilities in our <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_lsp">LSP (Language Server Protocol)</a>, or add new features in one of our editor extensions: <a href="https://github.com/biomejs/biome-vscode">VS Code</a>, <a href="https://github.com/biomejs/biome-zed">Zed</a> and <a href="https://github.com/biomejs/biome-intellij">JetBrains IntelliJ</a>.</li>
</ul>
<div><h4 id="financial-help">Financial help</h4></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program</a> that allows companies to employ one of the core contributors to work on a specific aspect of the Biome toolchain.</p>Biome v2.3—Let's bring the ecosystem closerhttps://biomejs.dev/blog/biome-v2-3/https://biomejs.dev/blog/biome-v2-3/Biome 2.3 brings full support (experimental) for Vue, Svelte and Astro, new syntax to ignore paths, new CLI flags, new formatting options, new reporters and more.
Tue, 07 Oct 2025 00:00:00 GMT<p>We’re excited to announce the release of Biome 2.3, bringing several features that have been highly requested by the community. This release marks a significant milestone in our journey to support the broader web ecosystem.</p>
<p>Once you have upgraded to Biome v2.3.0, migrate your Biome configuration to the new version by running the <code dir="auto">migrate</code> command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="full-support-for-vue-svelte-and-astro">Full support for Vue, Svelte, and Astro</h2></div>
<p>Biome 2.3 introduces full support for Vue, Svelte, and Astro files. This means you can now format and lint the JavaScript and TypeScript code inside <code dir="auto">&#x3C;script></code> tags, as well as the CSS inside <code dir="auto">&#x3C;style></code> tags in these frameworks. The HTML/template portions of these files are also parsed and formatted according to Biome’s HTML formatting rules.</p>
<p>This achievement wouldn’t have been possible without the great efforts of <span> <span>Core Contributor</span> <a href="https://github.com/ematipico" title="Member @ematipico"> <img src="https://biomejs.dev/\_astro/602478\_Z2a71bI.webp?dpl=69dce24b554af000071740e1" alt="Member @ematipico" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@ematipico</span> </a> </span> and <span> <span>Core Contributor</span> <a href="https://github.com/dyc3" title="Member @dyc3"> <img src="https://biomejs.dev/\_astro/1808807\_Z1eUQo7.webp?dpl=69dce24b554af000071740e1" alt="Member @dyc3" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@dyc3</span> </a> </span> .</p>
<p>This is a feature that many developers have been asking for, and we’re thrilled to finally deliver it. Achieving this has had its challenges, and it required extensive trials to get the architecture right based on the constraints of the toolchain.</p>
<p>However, this feature is marked as <strong>experimental</strong> for several important reasons. First, these frameworks have their own specific syntaxes and idioms that extend beyond standard HTML, CSS, and JavaScript. While we’ve done extensive work to handle many patterns, there are cases and framework-specific syntaxes that may not yet be fully supported (for example Svelte control-flow syntax, or Astro JSX-like syntax). We encourage you to avail of this new feature, and fine-tune it based on your needs and possible limitations found.</p>
<p>Please open a discussion if you find something that hasn’t been implemented, or an issue if there’s a parsing error that should be handled correctly.</p>
<p>To enable the feature, you’ll have to opt in the new <code dir="auto">html.experimentalFullSupportEnabled</code> option:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"html"</span><span>: {</span></div></div><div><div><span> </span><span>"</span><ins><span>experimentalFullSupportEnabled</span></ins><span>"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<aside aria-label="Note"><p aria-hidden="true">Note</p><div><p>We plan to fade out this option and make it the default. The option will be removed once the HTML parser becomes stable and supports more language-specific features.</p></div></aside>
<div><h3 id="script-and-style-indentation">Script and style indentation</h3></div>
<p>Additionally, you can configure specific formatting options for HTML content, such as whether to indent the content of <code dir="auto">&#x3C;script></code> and <code dir="auto">&#x3C;style></code> tags:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"html"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"</span><ins><span>indentScriptAndStyle</span></ins><span>"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span>file.vue</span></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>script</span></span><span> </span><span>setup</span><span> </span><span>lang</span><span>=</span><span>"</span><span>ts</span><span>"</span><span>></span></div></div><div><div><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span> </span><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span><span>&#x3C;/</span><span>script</span><span>></span></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span>file.svelte</span></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>script</span><span> </span></span><span>lang</span><span>=</span><span>"</span><span>ts</span><span>"</span><span>></span></div></div><div><div><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span> </span><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span><span>&#x3C;/</span><span>script</span><span>></span></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span>file.astro</span></figcaption><pre><code><div><div><span>---</span></div></div><div><div><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span> </span><span>const </span><span>foo</span><span> = </span><span>"</span><span>bar</span><span>"</span><span>;</span></div></div><div><div><span>---</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>By default, <code dir="auto">indentScriptAndStyle</code> is set to <code dir="auto">false</code> to match Prettier’s behavior.</p>
<div><h3 id="possible-inconsistencies">Possible inconsistencies</h3></div>
<p>With this release, we step into something new that needs to be addressed and discussed. In Biome you can configure each language as you see fit, which means that a project <em>might end up with different formatting (as example)</em>.</p>
<p>In the following configuration file, JavaScript files are formatted using double quotes, while CSS files are formatted using single quotes.</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"html"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: { </span><span>"enabled"</span><span>: </span><span>true</span><span> },</span></div></div><div><div><span> </span><span>"experimentalFullSupportEnabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"javascript"</span><span> : {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"quoteStyle"</span><span>: </span><span>"</span><span>double</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"css"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"quoteStyle"</span><span>: </span><span>"</span><span>single</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Why would someone want that? That’s not for us to answer, however with a configuration like this you would end with <strong>different quotes inside your HTML-ish files</strong>.
This could cause inconsistencies inside the same. We created a <a href="https://github.com/biomejs/biome/discussions/7754">GitHub discussion</a> to understand if this is a problem, and if so, how Biome should solve it. Please let us know what do you think.</p>
<div><h2 id="new-ignore-syntax">New ignore syntax</h2></div>
<p>Biome 2.3 introduces a refined syntax for ignoring paths in your project, addressing important problems that arose since the introduction of multi file analysis and TypeScript inference.</p>
<p>When Biome 2.0 came out, we internally introduced the concept of “paths being indexed”. When a path is indexed, Biome parses it and updates the module graph and the type inference, if enabled.</p>
<p>However, we slowly came to the realization that multi-file analysis and type inference are very complex problems that can get out of hand easily.</p>
<p>For example, type inference can enter a very nasty loop where tons of types are recursively indexed, consuming a lot of memory.</p>
<p>As for multi-file analysis, the <code dir="auto">node\_modules/</code> folder can be a rabbit hole, full of symbolic links with high depths and path names that exceed the maximum allowed characters.</p>
<p>Solving these complex problems takes time, a lot of testing and patience from us and the community. With this new syntax, users have now more control over what Biome can and can’t do.</p>
<p>With this release, two syntaxes are now available:</p>
<ul>
<li><code dir="auto">!</code> (single exclamation mark): Ignores the path from linting and formatting, but still allows it to be indexed by the type system. This is useful for generated files or third-party code that you don’t want to format or lint, but still need for type inference and imports.</li>
<li><code dir="auto">!!</code> (double exclamation mark): Completely ignores the path from all Biome operations, including type indexing. This is useful for files that should be entirely excluded from Biome’s analysis, such as <code dir="auto">dist/</code> folders.</li>
</ul>
<p>This distinction is particularly important when working with TypeScript projects that rely on type inference from dependencies or generated code. By using <code dir="auto">!</code>, you can exclude these files from formatting and linting while still maintaining correct type information across your project.</p>
<p>Here’s an example configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"files"</span><span>: {</span></div></div><div><div><span> </span><span>"includes"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>\*\*</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"</span><span>!\*\*/generated</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"</span><ins><span>!!</span></ins><span>\*\*/dist</span><span>"</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>In this configuration, files in the <code dir="auto">generated/</code> directory are ignored for formatting and linting but remain indexed for types and module graph, while files in <code dir="auto">dist/</code> directory are completely excluded from all Biome operations.</p>
<p>This is an important tool <strong>at your disposal</strong> that allows you to control Biome, and <a href="https://github.com/biomejs/biome/issues/7173">avoid</a> <a href="https://github.com/biomejs/biome/issues/7240">possible</a> <a href="https://github.com/biomejs/biome/issues/7007">slowness</a> and <a href="https://github.com/biomejs/biome/issues/6797">memory</a> <a href="https://github.com/biomejs/biome/issues/7020">leaks</a>.</p>
<p>As result, the option <code dir="auto">files.experimentalScannerIgnores</code> has been <strong>deprecated</strong>. We plan to remove this option in the next releases. Run the <code dir="auto">biome migrate</code> command update your configuration file.</p>
<p>Great shoutout to <span> <span>Core Contributor</span> <a href="https://github.com/arendjr" title="Member @arendjr"> <img src="https://biomejs.dev/\_astro/533294\_1AFeci.webp?dpl=69dce24b554af000071740e1" alt="Member @arendjr" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@arendjr</span> </a> </span> for implementing this new feature.</p>
<div><h2 id="tailwind-v4-support">Tailwind v4 support</h2></div>
<p><span> <span>Core Contributor</span> <a href="https://github.com/dyc3" title="Member @dyc3"> <img src="https://biomejs.dev/\_astro/1808807\_Z1eUQo7.webp?dpl=69dce24b554af000071740e1" alt="Member @dyc3" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@dyc3</span> </a> </span> worked really hard, and he shipped for us <strong>native support</strong> of tailwind files!</p>
<p>This is a opt-in feature of the CSS parser, and you can enable it using the new <code dir="auto">css.parser.tailwindDirectives</code> option:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"css"</span><span>: {</span></div></div><div><div><span> </span><span>"parser"</span><span>: {</span></div></div><div><div><span> </span><span>"tailwindDirectives"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span>tailwind.css</span></figcaption><pre><code><div><div><span>@utility</span><span> container {</span></div></div><div><div><span> </span><span>margin-inline</span><span>: auto;</span></div></div><div><div><span> </span><span>padding-inline</span><span>: 2rem;</span></div></div><div><div><span>}</span></div></div><div><div><span>@theme</span><span> {</span></div></div><div><div><span> </span><span>--color-</span><span>\*</span><span>: intial;</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="lint-rules">Lint rules</h2></div>
<div><h3 id="promoted-rules">Promoted rules</h3></div>
<ul>
<li>Promoted <code dir="auto">noNonNullAssertedOptionalChain</code> to the suspicious group</li>
<li>Promoted <code dir="auto">useReactFunctionComponents</code> to the <code dir="auto">style</code> group</li>
<li>Promoted <code dir="auto">useImageSize</code> to the <code dir="auto">correctness</code> group</li>
<li>Promoted <code dir="auto">useConsistentTypeDefinitions</code> to the <code dir="auto">style</code> group</li>
<li>Promoted <code dir="auto">useQwikClasslist</code> to the <code dir="auto">correctness</code> group</li>
<li>Promoted <code dir="auto">noSecrets</code> to the <code dir="auto">security</code> group</li>
</ul>
<div><h3 id="removed-rules">Removed rules</h3></div>
<p>Removed nursery lint rule <code dir="auto">useAnchorHref</code>, because its use case is covered by <code dir="auto">useValidAnchor</code>.</p>
<div><h3 id="updated-the-react-domain">Updated the <code dir="auto">react</code> domain</h3></div>
<p>The following rules are now a part of the <code dir="auto">react</code> domain, and they won’t be enabled automatically unless you enabled the domain, or Biome detects <code dir="auto">react</code> as a dependency of your closest <code dir="auto">package.json</code>:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-children-prop/"><code dir="auto">lint/correctness/noChildrenProp</code></a> (recommended)</li>
<li><a href="https://biomejs.dev/linter/rules/no-react-prop-assignments/"><code dir="auto">lint/correctness/noReactPropAssignments</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-dangerously-set-inner-html/"><code dir="auto">lint/security/noDangerouslySetInnerHtml</code></a> (recommended)</li>
<li><a href="https://biomejs.dev/linter/rules/no-dangerously-set-inner-html-with-children/"><code dir="auto">lint/security/noDangerouslySetInnerHtmlWithChildren</code></a> (recommended)</li>
<li><a href="https://biomejs.dev/linter/rules/use-component-export-only-modules/"><code dir="auto">lint/style/useComponentExportOnlyModules</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-array-index-key/"><code dir="auto">lint/suspicious/noArrayIndexKey</code></a> (recommended)</li>
</ul>
<div><h2 id="improved---skip-and---only-flags">Improved <code dir="auto">--skip</code> and <code dir="auto">--only</code> flags</h2></div>
<p>The flags <code dir="auto">--skip</code> and <code dir="auto">--only</code> have been enhanced, and they can accept <a href="https://biomejs.dev/linter/domains">lint domains</a> too.</p>
<p>In the following example, the <code dir="auto">lint</code> command runs only the rules that belong to the <code dir="auto">project</code> domain:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--only=project</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>In the following example, the <code dir="auto">lint</code> command runs all the rules that you configured, expect for the rules that belong to the <code dir="auto">test</code> domain:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--skip=test</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="enhanced-init-command">Enhanced <code dir="auto">init</code> command</h2></div>
<p>The <code dir="auto">init</code> command now checks if the project contains ignore files and <code dir="auto">dist/</code> folders. If supported ignore files are found, Biome will
enable the <a href="https://biomejs.dev/guides/integrate-in-vcs">VCS integration</a>, and if <code dir="auto">dist/</code> folder is found, it will exclude it using the new ignore syntax. This should help reducing
the friction when starting with Biome:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"vcs"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"clientKind"</span><span>: </span><span>"</span><span>git</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useIgnoreFile"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="new-reporters">New reporters</h2></div>
<p>Two new CLI reporters have been added:</p>
<ul>
<li><a href="https://checkstyle.org/">checkstyle reporter</a> via the new option <code dir="auto">--reporter=checkstyle</code></li>
<li><a href="https://reviewdog.github.io/rdjson-viewer/?rdjson=eJztmU1z2jAQhu%2F5FRpfcgm4pA1NmMmhnzOZ6altcun0IKw1qCNLVJJJSIb%2F3pVtCKQYDAPBYHOyZe1afh%2FvrhY%2FnRDiGRXrALwOecIzPJc0cmfeR67w4CwdjLVwY31rB6bj%2B1137Y9pMhh6OGHsZnmM055UxvLA4NxfiWHqEy8Gij3fY4VLX3BpQfs6FmB8qRqxjA2wBo8GSluTrSlxMqQiTlbrTPxAaQ2BlWCc2W1idZMZZTbjibEnVEAtV3J%2BVQNq%2B84flwwemvM301T25h8CB0GyF0PJ04o4cp5b52fzV3CdzkVrZnQ8O8Uzlmq7xONlAYcnL4%2BenzpCbWjyFN7PPjck1ZTgUSpyMxUqM6g8vtZitc83xtd6U8BjMX4%2FYAiaCqJCYvtgIGNpCNWwe5pDqjnt4th6PO%2BmZvsh2l4s%2F%2BXGQC8KOFwjHieykvBVYvJAKeYkwauNKb4v4LC8FF8zs0aUy7ouVpxeXRbLklC3A7SuikcAsapFkRrDjfVp4AQ2vtI9KvkjLM2rmU3a%2B05N9ttsnOdk1c1rYhGHRQHO5FHJCDw851SpLDF4tpuQZCrGd6YBf2MqlsSjic2AB1zFzuhzYvMlNdkPzJwE%2BG5jlm8LOCzG8tZw2SPX1ySiI9J1NdHQEPGGZKTihKgGMXJzlCR2NAASKNCordwJX%2BjGvR7oomgn0%2FeD9Woxhfa2Q7S9PtZ02%2BrCE4lifGJ1AkYwyWY7ITJRmuCaLEQg7S54YpYQSMs2qBw1BNiCXG8ysw9y9A2N9kP3YLZBE5HFiPSpSeii3Emw1kznERzMruiVmWpgEAjM9gVhfp%2FO3w%2FHcvecfRULJk8tmcpKTh9Pm%2BQT7kg5w5xrFeZfDB3kbInSOM99Z8GT5lQXz7j0bJJdrDf5gOJ%2Bcyotki5HvGXyLd4NvpAwV8RlMuZ6zgVl4cHdwkPFXAFjEKI9I33Q0PH%2BA%2FC7joUS57SFkRCWKRLaea%2Fr5fzrunYgXBR0vDoOwm3GwfQ9DpWO6IIyPEPvazIFY4PcO4xYiIZABtqFC0sqUqiEUPeuNwgUDkrbOYYGfjv%2Fv9T9exn69%2B2wrNv3crXv26Fad%2B%2Bl7PQq9g2jCs17xb5oHGvvXoXPxXXrvtpzLqjqtO5Hn9Hqzn2l49VhcICd%2B4lb0Pgf0iY3Ww%3D%3D">RDJSON reporter</a> via the new option <code dir="auto">--reporter=rdjson</code></li>
</ul>
<div><h2 id="new-cli-flags">New CLI flags</h2></div>
<p>We added the new CLI flags to better control Biome without relying on the configuration file. Here’s the list:</p>
<ul>
<li><code dir="auto">--format-with-errors</code>: CLI flag that allows to format code that contains parse errors.</li>
<li><code dir="auto">--css-parse-css-modules</code>: CLI flag to control whether CSS Modules syntax is enabled.</li>
<li><code dir="auto">--css-parse-tailwind-directives</code>: CLI flag to control whether Tailwind CSS 4.0 directives and functions are enabled.</li>
<li><code dir="auto">--json-parse-allow-comments</code>: CLI flag to control whether comments are allowed in JSON files.</li>
<li><code dir="auto">--json-parse-allow-trailing-commas</code>: CLI flag to control whether trailing commas are allowed in JSON files.</li>
</ul>
<div><h2 id="lineending-format-option"><code dir="auto">lineEnding</code> format option</h2></div>
<p>The option <code dir="auto">lineEnding</code> now has a variant called <code dir="auto">auto</code> to match the operating system’s expected
line-ending style: on Windows, this will be CRLF (<code dir="auto">\r\n</code>), and on macOS / Linux, this will
be LF (<code dir="auto">\n</code>).</p>
<p>This allows for cross-platform projects that use Biome not to have to
force one option or the other, which aligns better with Git’s default behavior
on these platforms.</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"lineEnding"</span><span>: </span><ins><span>"</span><span>auto</span><span>"</span></ins></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--line-ending</span><span> </span><span>auto</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="and-more">And more!</h2></div>
<p>More features and fixes have been shipped, like React v19 support, <code dir="auto">baseUrl</code> support inside <code dir="auto">tsconfig.json</code>, and more. Refer to the changelog page for a <a href="https://biomejs.dev/internals/changelog/version/2-3-0/">detailed breakdown of the features</a>.</p>
<div><h2 id="i-like-where-this-is-going-how-can-i-help">I like where this is going, how can I help?</h2></div>
<p>I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h4 id="translations">Translations</h4></div>
<p>If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this <a href="https://biomejs.dev/i18n-dashboard/">dashboard</a>, you can check the supported languages and if they are up to date.</p>
<div><h4 id="chat-with-us">Chat with us</h4></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. Chatting with the community and being part of the community is a form of contribution.</p>
<div><h4 id="code-contributions">Code contributions</h4></div>
<p>If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!</p>
<p>There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:</p>
<ul>
<li>Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very <a href="https://github.com/biomejs/biome/blob/main/crates/biome\_analyze/CONTRIBUTING.md">extensive technical guide</a>.</li>
<li><a href="https://github.com/biomejs/biome/blob/main/crates/biome\_parser/CONTRIBUTING.md">Help</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_yaml\_parser">building</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_html\_parser">Biome</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_markdown\_parser">parsers</a>!
One interesting fact about Biome parsers is that they are recoverable parsers <a href="https://biomejs.dev/internals/architecture/#parser-and-cst">error resilient</a> which emit a <a href="https://en.wikipedia.org/wiki/Parse\_tree">CST</a> instead of a classic AST.</li>
<li>Implement new capabilities in our <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_lsp">LSP (Language Server Protocol)</a>, or add new features in one of our editor extensions: <a href="https://github.com/biomejs/biome-vscode">VS Code</a>, <a href="https://github.com/biomejs/biome-zed">Zed</a> and <a href="https://github.com/biomejs/biome-intellij">JetBrains IntelliJ</a>.</li>
</ul>
<div><h4 id="financial-help">Financial help</h4></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program </a> where a company you can employ one of the core contributors to work a specific aspect of the Biome toolchain.</p>Biome v2.1https://biomejs.dev/blog/biome-v2-1/https://biomejs.dev/blog/biome-v2-1/Biome 2.1 has been released with many bugfixes, a faster scanner, and improved type inference.
Tue, 08 Jul 2025 00:00:00 GMT<p>Biome 2.0 was released less than a month ago, and since then we have seen an
amazing uptake! Our Discord is buzzing, our downloads are spiking, and bugs are
rolling in :)</p>
<div><h2 id="faster-scanner">Faster scanner</h2></div>
<p>Probably the main point of contention is that Biome 2.0 introduced a new
scanner, which we use for discovering nested configuration files as well as for
populating our module graph, if project rules are enabled. The reason for this
contention is that having a scanner makes things slower, while people want Biome
to be fast.</p>
<p>To mitigate the impact, we already made the project rules opt-in for 2.0, so
that users can choose between features and speed for themselves. But ideally,
we’d have both. And unfortunately, even without project rules, the scanner still
caused <em>some</em> noticeable overhead.</p>
<p>For Biome 2.1 we’re changing the logic for how the “light scanner” (the one
where project rules are disabled) works. Previously, it would always scan the
entire project from its root, whereas now it will use the files and folders that
you ask Biome to operate on as a hint for which parts of the project should be
scanned.</p>
<p>This means if you run Biome without any arguments from the project root, you are
not going to notice a difference. But if you specify specific files to check, or
if you run Biome inside a nested folder, the scanner will know which parts of
the project you are interested in, and only scan those.</p>
<p>Note that if you have enabled project rules, these improvements don’t apply.
This is because project rules often need to pull information from other files,
<em>including ones you didn’t specify</em>, so we still scan the entire project for
now.</p>
<div><h2 id="improved-type-inference">Improved type inference</h2></div>
<p>When we released Biome 2.0, we mentioned that our type inference was able to
detect ~75% of cases that our
<a href="https://biomejs.dev/linter/rules/no-floating-promises/"><code dir="auto">noFloatingPromises</code> rule</a>
should ideally detect. Since then, we’ve been able to improve this to ~85%, and
cases such as these can now be successfully inferred:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>// We know that this evaluates to a `Promise`:</span></div></div><div><div><span>true</span><span> </span><span>&#x26;&#x26;</span><span> </span><span>Promise</span><span>.</span><span>reject</span><span>(</span><span>"</span><span>logical operator bypass</span><span>"</span><span>);</span></div></div><div><div>
</div></div><div><div><span>// But this doesn't:</span></div></div><div><div><span>false</span><span> </span><span>&#x26;&#x26;</span><span> </span><span>Promise</span><span>.</span><span>reject</span><span>(</span><span>"</span><span>logical operator bypass</span><span>"</span><span>);</span></div></div><div><div>
</div></div><div><div><span>// Similarly, we now detect that this may return a `Promise`:</span></div></div><div><div><span>const </span><span>condition</span><span> = </span><span>Math</span><span>.</span><span>random</span><span>()</span><span> > -</span><span>1</span><span>; </span><span>// Always true, but dynamic to linter</span></div></div><div><div><span>condition </span><span>?</span><span> </span><span>Promise</span><span>.</span><span>reject</span><span>(</span><span>"</span><span>ternary bypass</span><span>"</span><span>) </span><span>:</span><span> </span><span>null</span><span>;</span></div></div><div><div>
</div></div><div><div><span>// On the other hand, we know the following is never a `Promise`:</span></div></div><div><div><span>const </span><span>alwaysFalsy</span><span> = </span><span>0</span><span>;</span></div></div><div><div><span>alwaysFalsy </span><span>?</span><span> </span><span>Promise</span><span>.</span><span>reject</span><span>(</span><span>"</span><span>ternary bypass</span><span>"</span><span>) </span><span>:</span><span> </span><span>null</span><span>;</span></div></div><div><div>
</div></div><div><div><span>// This will now get flagged because the `Promise`s are not handled:</span></div></div><div><div><span>[</span><span>1</span><span>, </span><span>2</span><span>, </span><span>3</span><span>]</span><span>.</span><span>map</span><span>(</span><span>async</span><span> </span><span>(</span><span>x</span><span>)</span><span> </span><span>=></span><span> x </span><span>+</span><span> </span><span>1</span><span>);</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Additionally, we have added support for getters, call signatures, comma
operators, and more. Our goal is for you to not have to worry about which parts
of TypeScript are supported, and the vast majority of cases to “just work”. It’s
still a work in progress, but we’re happy with the progress we are seeing.</p>
<p>And finally we have also added the related rule
<a href="https://biomejs.dev/linter/rules/no-misused-promises/"><code dir="auto">noMisusedPromises</code></a>.</p>
<div><h2 id="rule-updates">Rule updates</h2></div>
<p>The following new rules have been added in 2.1.0:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-alert/"><code dir="auto">noAlert</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-implicit-coercion/"><code dir="auto">noImplicitCoercion</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-magic-numbers/"><code dir="auto">noMagicNumbers</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misused-promises/"><code dir="auto">noMisusedPromises</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unassigned-variables/"><code dir="auto">noUnassignedVariables</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-readonly-class-properties/"><code dir="auto">useReadonlyClassProperties</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-unified-type-signature/"><code dir="auto">useUnifiedTypeSignature</code></a></li>
</ul>
<p>Other notable change:</p>
<ul>
<li>The rule
<a href="https://biomejs.dev/linter/rules/no-unused-function-parameters/"><code dir="auto">noUnusedFunctionParameters</code></a>
has been enhanced with an <code dir="auto">ignoreRestSiblings</code> option.</li>
</ul>
<div><h2 id="notable-bug-fixes">Notable bug fixes</h2></div>
<ul>
<li>If you ignore a nested configuration file from your root configuration, it
will now be properly ignored.</li>
<li>When extending a configuration from another, we now correctly ignore the
<code dir="auto">root</code> of the other configuration. This one led to some confusion in several
use cases.</li>
</ul>
<div><h2 id="whats-next">What’s next</h2></div>
<p>It’s still early days in our 2.x journey. Both the scanner are type inference
are likely to see further improvements. Additionally, our
<a href="https://biomejs.dev/internals/people-and-credits#core-contributors">Core Contributors</a> will focus
on moving forward the <a href="https://biomejs.dev/blog/roadmap-2025#-2025-roadmap">Roadmap for 2025</a>, and
focus on the following features:</p>
<ul>
<li>Make HTML support stable.</li>
<li>Expand HTML to support other frameworks such as Vue, Svelte, Astro and,
hopefully, Angular too.</li>
<li>Work on Markdown support, starting from the parser.</li>
<li>and more!</li>
</ul>
<div><h2 id="installation-and-migration">Installation and migration</h2></div>
<p>Install or update the <code dir="auto">@biomejs/biome</code> package. If you upgrade the package, run
the <code dir="auto">migrate</code> command.</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome</span></div></div><div><div><span>npx</span><span> </span><span>@biomejs/biome</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The <code dir="auto">migrate</code> command takes care of breaking changes of the configuration, so
you don’t have to.</p>
<aside aria-label="Note"><p aria-hidden="true">Note</p><div><p>If you are upgrading from Biome 1.x, please follow the
<a href="https://biomejs.dev/guides/upgrade-to-biome-v2">migration guide</a> and upgrade to Biome 2.0 first,
before upgrading to Biome 2.1.</p></div></aside>
<div><h2 id="i-like-where-this-is-going-how-can-i-help">I like where this is going, how can I help?</h2></div>
<p>Biome is a project led by volunteers who like programming, open-source, and
embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h3 id="translations">Translations</h3></div>
<p>If you are familiar with Biome and would like to contribute to its outreach, you
can assist us by translating the website into your native language. In this
<a href="https://biomejs.dev/i18n-dashboard/">dashboard</a>, you can check the supported
languages and if they are up to date.</p>
<div><h3 id="chat-with-us">Chat with us</h3></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the
community. Chatting with the community and being part of the community is a form
of contribution.</p>
<div><h3 id="code-contributions">Code contributions</h3></div>
<p>If you like the technical aspects of the project, and you want to make your way
into the Rust language, or practice your knowledge around parsers, compilers,
analysers, etc., Biome is the project that does for you!</p>
<p>There are numerous aspects to explore; I assure you that you won’t get bored.
Here is a small list of the things you can start with:</p>
<ul>
<li>Create new lint rules! We have so many rules that we haven’t implemented yet
(ESLint, ESLint plugins, Next.js, Solid, etc.). We have an <a href="https://github.com/biomejs/biome/blob/main/crates/biome\_analyze/CONTRIBUTING.md">extensive
technical
guide</a>.</li>
<li><a href="https://github.com/biomejs/biome/blob/main/crates/biome\_parser/CONTRIBUTING.md">Help</a>
<a href="https://github.com/biomejs/biome/tree/main/crates/biome\_yaml\_parser">building</a>
<a href="https://github.com/biomejs/biome/tree/main/crates/biome\_html\_parser">Biome</a>
<a href="https://github.com/biomejs/biome/tree/main/crates/biome\_markdown\_parser">parsers</a>!
One interesting fact about Biome parsers is that they are recoverable parsers
<a href="https://biomejs.dev/internals/architecture/#parser-and-cst">error resilient</a> which emit a
<a href="https://en.wikipedia.org/wiki/Parse\_tree">CST</a> instead of a classic AST.</li>
<li>Implement new capabilities in our <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_lsp">LSP (Language Server
Protocol)</a>, or
add new features in one of our editor extensions: <a href="https://github.com/biomejs/biome-vscode">VS
Code</a>,
<a href="https://github.com/biomejs/biome-zed">Zed</a> and <a href="https://github.com/biomejs/biome-intellij">JetBrains
IntelliJ</a>.</li>
</ul>
<div><h3 id="financial-help">Financial help</h3></div>
<p>If you believe in the future of the project, you can also help with a financial
Sponsors</a>.</p>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program </a>
where as a company you can contract one of the core contributors to work on a
specific aspect of the Biome toolchain.</p>Biome v2—codename: Biotypehttps://biomejs.dev/blog/biome-v2/https://biomejs.dev/blog/biome-v2/Biome 2.0 is officially out, as the first JavaScript linter that provides type-aware linting rules
that don't rely on the TypeScript compiler. With this release, Biome also ships plugin support, multi-file analysis,
revamped import sorting, experimental HTML formatting, better suppressions, better LSP support, and more!
Tue, 17 Jun 2025 00:00:00 GMT<p>We are happy to announce that Biome v2 is officially out! 🍾 Biome v2—codename: Biotype, the <em>first</em> JavaScript and TypeScript linter that provides
<strong>type-aware linting rules that doesn’t rely on the TypeScript compiler</strong>! This means that you can lint your project
without necessarily installing the <code dir="auto">typescript</code> package.</p>
<p>With this release, the <a href="https://biomejs.dev/internals/people-and-credits#core-contributors">Core Contributors of the project</a> want to show
to the whole community and web ecosystem that Biome is here to stay and deserves to earn its place as the next-generation toolchain for the web.
No other tools have achieved this great milestone in such a short amount of time (<a href="https://biomejs.dev/blog/announcing-biome">two years</a>) and resources. This has been possible
thanks to the companies and people who believed in the project, with a special shoutout to <a href="https://vercel.com/">Vercel</a> for sponsoring the type inference work.</p>
<p>Preliminary testing shows that our <a href="https://biomejs.dev/linter/rules/no-floating-promises/"><code dir="auto">noFloatingPromises</code> rule</a>, which is based on our new type inference work, can detect floating promises in about 75% of the cases that would be detected by using <code dir="auto">typescript-eslint</code>, at a fraction of the performance impact. And needless to say, we have plenty of ideas on how to improve this metric even further.</p>
<p>Keep in mind that your mileage may vary, as these early numbers are based on a limited set of use cases. Nevertheless, we look forward to people trying it out and reporting their experiences so that we can quickly reach a level of confidence that would be sufficient for most projects.</p>
<div><h2 id="installation-and-migration">Installation and migration</h2></div>
<p>Install or update the <code dir="auto">@biomejs/biome</code> package. If you upgrade the package, run the <code dir="auto">migrate</code> command.</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome</span></div></div><div><div><span>npx</span><span> </span><span>@biomejs/biome</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The <code dir="auto">migrate</code> command will take care of all the breaking changes of the configuration, so you don’t have to. However, there are
some other changes that we couldn’t automate. We created a <a href="https://biomejs.dev/guides/upgrade-to-biome-v2">migration guide</a> that explains them,
together with manual migration paths, if applicable. Please get accustomed to the changes, as some of them fundamentally
change some of the core functionalities of Biome (for the better!).</p>
<div><h2 id="relevant-features">Relevant features</h2></div>
<p>Biome is packed with new features, some big and some small. We will focus on the ones that we believe are worth
mentioning. For a complete list of the new features, refer to the <a href="https://biomejs.dev/internals/changelog">web version of the changelog</a>.</p>
<div><h3 id="multi-file-analysis-and-type-inference">Multi-file analysis and type inference</h3></div>
<p>These two features are closely related. You can’t create a type inference engine without the ability to query types imported from
other modules.</p>
<p>Before version 2.0, Biome lint rules could only operate on one file at a time. This brought us far, but many of the more interesting rules require information from other files too.</p>
<p>To accomplish this, we have added a <em>file scanner</em> to Biome that scans all the files in your project and indexes them, similar to what an LSP service might do in your IDE.</p>
<p>A file scanner comes with its baggage: slowness. We acknowledge that many users choose Biome for its speed. During the beta period, users raised some concerns about how this could affect their workflow.</p>
<p>As for this release, the file scanner has the following characteristics:</p>
<ul>
<li>It’s <strong>opt-in</strong>; which means migrating from v1 to v2 won’t significantly affect the performance of formatting and linting your projects.</li>
<li>By default, the scanner is only used for discovering nested configuration files. This should be very fast, although a slight increase compared to v1 may be experienced.</li>
<li>A <strong>full scan</strong> (which scans all your project files <strong>and</strong> <code dir="auto">node\_modules</code>) is performed <em>only</em> when <a href="https://biomejs.dev/linter/domains#project">project rules</a> are enabled.</li>
<li>Users can control the scanned files using <code dir="auto">files.includes</code>, with the exception of <code dir="auto">node\_modules</code>.</li>
<li>Lint rules that need to collect types or query the module graph <strong>will never be recommended</strong> outside the <a href="https://biomejs.dev/linter/domains/#project"><code dir="auto">project</code> domain</a>. We put speed and performance first, and users have control over the rules.</li>
</ul>
<div><h3 id="monorepo-support">Monorepo Support</h3></div>
<p>We’ve significantly improved our support for monorepos. This means that lint rules that rely on information from <code dir="auto">package.json</code> files will now use the <code dir="auto">package.json</code> from the right package. But perhaps more importantly: <strong>We now support nested configuration files.</strong></p>
<p>Every project should still have a single <code dir="auto">biome.json</code> or <code dir="auto">biome.jsonc</code> at its root, similar to Biome v1. But projects are allowed to have any number of nested <code dir="auto">biome.json</code>/<code dir="auto">biome.jsonc</code> files in subdirectories. Nested configuration files must be explicitly marked as such, in one of two ways.</p>
<p>The first looks like this:</p>
<div><figure><figcaption><span>biome.jsonc</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"root"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>// ...</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>By setting the <code dir="auto">root</code> field to <code dir="auto">false</code>, you tell Biome this is a nested file. This is important, because if you run Biome inside the nested folder, it will know that the configuration is part of a bigger project and continue looking for the root configuration as well.</p>
<p>It is important to stress that the settings within the nested folder <strong>do not</strong> inherit from the root settings by default. Rather, we still want you to use the <a href="https://biomejs.dev/guides/big-projects/#share-the-configuration"><code dir="auto">extends</code> field</a> that already existed in Biome v1 if you want to extend from another configuration.</p>
<p>Which brings us to the second way a nested configuration can be defined:</p>
<div><figure><figcaption><span>biome.jsonc</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"extends"</span><span>: </span><span>"</span><span>//</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>// ...</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>This is a convenient micro-syntax that sets both the <code dir="auto">root</code> field to <code dir="auto">false</code>, and will tell Biome that this nested configuration extends from the root configuration.</p>
<p>Say goodbye to wonky relative paths such as <code dir="auto">"extends": ["../../biome.json"]</code> 👋</p>
<p>We prepared a <a href="https://biomejs.dev/guides/big-projects#monorepo">small guide</a> that should help you set everything up.</p>
<div><h3 id="plugins">Plugins</h3></div>
<p>Biome 2.0 comes with our first iteration of <a href="https://biomejs.dev/linter/plugins">Linter Plugins</a>.</p>
<p>These plugins are still limited in scope: They only allow you to match code snippets and report diagnostics on them.</p>
<p>Here is an example of a plugin that reports on all usages of <code dir="auto">Object.assign()</code>:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>`$fn($args)` where {</span></div></div><div><div><span><span> </span></span><span>$fn &#x3C;: `Object.assign`,</span></div></div><div><div><span><span> </span></span><span>register\_diagnostic(</span></div></div><div><div><span><span> </span></span><span>span = $fn,</span></div></div><div><div><span><span> </span></span><span>message = "Prefer object spread instead of `Object.assign()`"</span></div></div><div><div><span><span> </span></span><span>)</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>It’s a first step, but we have plenty of ideas for making them more powerful, and we’re eager to hear from our users about what they would like to see prioritised.</p>
<p>As for now, we intentionally left out the distribution method of plugin for different reasons. However, we would like to hear from you. Please <a href="https://github.com/biomejs/biome/discussions/6265">join the discussion</a> and share your ideas with us.</p>
<div><h3 id="import-organizer-revamp">Import Organizer Revamp</h3></div>
<p>In Biome 1.x, our Import Organizer had several limitations:</p>
<ul>
<li>
<p>Groups of imports separated by a blank line were considered separate <em>chunks</em>, meaning they were sorted independently. This meant the following <strong>didn’t work</strong> as expected:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>It would correctly sort <code dir="auto">"library1"</code> to be placed above <code dir="auto">"./utils.js"</code>, but it wouldn’t be able to
carry it over the blank line to the top. This is what we got:</p>
<div><figure><figcaption><span>organizer\_v1.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>But instead, what we really wanted was this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>Imports from the same module were not merged. Consider the following example:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> { util1 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { util2 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>What we wanted was this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { util1, util2 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>No custom ordering could be configured. Perhaps you didn’t really like the default approach of ordering by “distance” from the source that you’re importing from. Perhaps you wanted to organise the imports like this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { open } </span><span>from</span><span> </span><span>"</span><span>node:fs</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { internalLib1 } </span><span>from</span><span> </span><span>"</span><span>@company/library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { internalLib2 } </span><span>from</span><span> </span><span>"</span><span>@company/library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
</ul>
<p>In Biome 2.0, all these limitations are lifted. In fact, if you look at the examples above, all snippets labeled <code dir="auto">organizer\_v2.js</code> can be produced just like that by our new import organizer.</p>
<p>Other improvements include support for organizing <code dir="auto">export</code> statements, support for “detached” comments to explicitly separate import chunks if necessary, and import attribute sorting.</p>
<p>You can find more in the <a href="https://biomejs.dev/assist/actions/organize-imports">documentation of the action</a>.</p>
<div><h3 id="assists">Assists</h3></div>
<p>The Import Organizer has always been a bit of a special case in Biome. It was neither part of the linter, nor of the formatter. This was because we didn’t want it to show diagnostics like the linter does, and its organizing features exceeded what we expect from the formatter.</p>
<p>In Biome 2.0, we have generalised such use cases in the form of Biome Assist. Assist provides <strong>actions</strong>, which are similar to the <em>fixes</em> in lint rules, but without the diagnostics.</p>
<p>The Import Organizer has become an assist, but we’ve started using this approach for new assists too: <a href="https://biomejs.dev/assist/actions/use-sorted-keys/"><code dir="auto">useSortedKeys</code></a> can sort keys in object literals, while <a href="https://biomejs.dev/assist/actions/use-sorted-attributes/"><code dir="auto">useSortedAttributes</code></a> can sort attributes in JSX.</p>
<p>For more information about assists, see <a href="https://biomejs.dev/assist/">the relative page</a>.</p>
<div><h3 id="improved-suppressions">Improved suppressions</h3></div>
<p>In addition to the <code dir="auto">// biome-ignore</code> comments we already supported, we now support <code dir="auto">// biome-ignore-all</code> for suppressing a lint rule or the formatter in an entire file.</p>
<p>We also added support for suppression ranges using <code dir="auto">// biome-ignore-start</code> and <code dir="auto">// biome-ignore-end</code>. Note that <code dir="auto">// biome-ignore-end</code> is optional in case you want to let a range run until the end of the file.</p>
<p>For more information about suppressions, see <a href="https://biomejs.dev/linter/#suppress-lint-rules">the relative page</a>.</p>
<div><h3 id="html-formatter">HTML formatter</h3></div>
<p>After several months of hard work, we are pleased to announce that the HTML formatter is now ready for users to try out and report bugs! This is a huge step towards Biome fully supporting HTML-ish templating languages used in frameworks such as Vue and Svelte.</p>
<p>For now, the HTML formatter only touches actual <code dir="auto">.html</code> files, so it doesn’t format HTML in <code dir="auto">.vue</code> or <code dir="auto">.svelte</code> files yet. It also won’t format embedded languages like JavaScript or CSS yet. HTML’s options like <code dir="auto">attributePosition</code>, <code dir="auto">bracketSameLine</code>, and <code dir="auto">whitespaceSensitivity</code> have been implemented.</p>
<p>The HTML formatter is still in the experimental stage, so it will remain <strong>disabled by default for the full 2.0 release</strong>. At the time of writing, Biome can parse most of the Prettier’s HTML test suite, and format 46/124 of them correctly. Despite not matching Prettier yet, we’re pretty confident that it <em>should</em> output adequately formatted documents without destroying anything. If you find a case where it doesn’t, <a href="https://github.com/biomejs/biome/issues">please let us know</a>!</p>
<p>You can enable the HTML formatter by adding the following to your config file:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"html"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="shout-outs">Shout-outs</h2></div>
<p>And now, let’s give credits where credits are due!</p>
<div><img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjQ2b3d6MjYzMTdsazdzcm41NmM1ZTMzaGcyM2xyeHo2N2k5NmxscyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QW5nKIoebG8y4/giphy.gif?dpl=69dce24b554af000071740e1" alt="it&#x27;s" loading="lazy" decoding="async" fetchpriority="auto" width="400" height="300"></div>
<div><a href="https://vercel.com" rel="nofollow" title="Vercel" target="\_blank"><img src="https://biomejs.dev/\_astro/vercel-logotype-dark.CrUgEJIc\_lXv46.webp?dpl=69dce24b554af000071740e1" alt="Vercel" data-canonical-src="/\_astro/vercel-logotype-dark.CrUgEJIc.png" loading="eager" decoding="async" fetchpriority="auto" width="500" height="113"><img src="https://biomejs.dev/\_astro/vercel-logotype-light.B4WmRf6j\_IWpP1.webp?dpl=69dce24b554af000071740e1" alt="Vercel" data-canonical-src="/\_astro/vercel-logotype-light.B4WmRf6j.png" loading="eager" decoding="async" fetchpriority="auto" width="500" height="113"></a></div>
<div><a href="https://depot.dev" rel="nofollow" title="Depot" target="\_blank"><img src="https://biomejs.dev/\_astro/depot-logo-horizontal-on-light@3x.CwT7\_\_a0\_Z1PxqHk.webp?dpl=69dce24b554af000071740e1" alt="Depot" data-canonical-src="/\_astro/depot-logo-horizontal-on-light@3x.CwT7\_\_a0.png" loading="eager" decoding="async" fetchpriority="auto" width="500" height="125"><img src="https://biomejs.dev/\_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV\_Z13t3VY.webp?dpl=69dce24b554af000071740e1" alt="Depot" data-canonical-src="/\_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV.png" loading="eager" decoding="async" fetchpriority="auto" width="500" height="125"></a></div>
<p>Congratulations to <span> <span>Core Contributor</span> <a href="https://github.com/siketyan" title="Member @siketyan"> <img src="https://biomejs.dev/\_astro/12772118\_Z1Vq2Pk.webp?dpl=69dce24b554af000071740e1" alt="Member @siketyan" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@siketyan</span> </a> </span> , who recently became a Core Contributor of the project! Thanks to their contributions,
the <a href="https://plugins.jetbrains.com/plugin/22761-biome">JetBrains extension</a> is now stable and supports multiple workspaces.</p>
<p>Thanks to <span> <span>Core Contributor</span> <a href="https://github.com/conaclos" title="Member @conaclos"> <img src="https://biomejs.dev/\_astro/2358560\_Z2aSQxu.webp?dpl=69dce24b554af000071740e1" alt="Member @conaclos" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@conaclos</span> </a> </span> for their massive work in implementing many features such as the Import Organizer revamping,
the new glob engine, many new linting rules.</p>
<p>Thanks to <span> <span>Core Contributor</span> <a href="https://github.com/arendjr" title="Member @arendjr"> <img src="https://biomejs.dev/\_astro/533294\_1AFeci.webp?dpl=69dce24b554af000071740e1" alt="Member @arendjr" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@arendjr</span> </a> </span> for creating the multi-file architecture, the continuous work on the type inference, plugins, and miscellaneous improvements.</p>
<p>Props to <span> <span>Core Contributor</span> <a href="https://github.com/nhedger" title="Member @nhedger"> <img src="https://biomejs.dev/\_astro/649677\_1HWtNb.webp?dpl=69dce24b554af000071740e1" alt="Member @nhedger" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@nhedger</span> </a> </span> for authoring the <a href="https://github.com/biomejs/setup-biome">GitHub Action</a>, and <a href="https://biomejs.dev/blog/2025-05-29-biome-vscode-v3/">shipping</a> the new version of the <a href="https://marketplace.visualstudio.com/items?itemName=biomejs.biome">VS Code extension</a>.</p>
<p>Thanks to <span> <span>Core Contributor</span> <a href="https://github.com/dyc3" title="Member @dyc3"> <img src="https://biomejs.dev/\_astro/1808807\_Z1eUQo7.webp?dpl=69dce24b554af000071740e1" alt="Member @dyc3" loading="lazy" decoding="async" fetchpriority="auto" width="25" height="25"> <span>@dyc3</span> </a> </span> for leading the work on the HTML parser and formatter. They are both very complex pieces of software, especially when it comes to matching Prettier’s formatting experience.</p>
<p>Last but not least, a great thanks to all our other <a href="https://github.com/biomejs/biome#sponsors">sponsors</a> and <a href="https://biomejs.dev/internals/people-and-credits#contributors">contributors</a> as well!</p>
<div><h2 id="whats-next">What’s next</h2></div>
<p>No software is exempt from bugs, so we will ensure that we squash them and release patches.</p>
<p>The <a href="https://biomejs.dev/internals/people-and-credits#core-contributors">Core Contributors</a> will focus on moving forward the <a href="https://biomejs.dev/blog/roadmap-2025#-2025-roadmap">Roadmap for 2025</a>, and focus on the following features:</p>
<ul>
<li>Make HTML support stable.</li>
<li>Expand HTML to support other frameworks such as Vue, Svelte, and Astro.</li>
<li>Work on Markdown support, starting from the parser.</li>
<li>Continue working on the inference infrastructure, so we can cover more cases and add new rules.</li>
<li>and more!</li>
</ul>
<div><h3 id="i-like-where-this-is-going-how-can-i-help">I like where this is going, how can I help?</h3></div>
<p>I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁</p>
<div><h4 id="translations">Translations</h4></div>
<p>If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this <a href="https://biomejs.dev/i18n-dashboard/">dashboard</a>, you can check the supported languages and if they are up to date.</p>
<div><h4 id="chat-with-us">Chat with us</h4></div>
<p>Join our <a href="https://biomejs.dev/chat">Discord server</a>, and engage with the community. Chatting with the community and being part of the community is a form of contribution.</p>
<div><h4 id="code-contributions">Code contributions</h4></div>
<p>If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!</p>
<p>There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:</p>
<ul>
<li>Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very <a href="https://github.com/biomejs/biome/blob/main/crates/biome\_analyze/CONTRIBUTING.md">extensive technical guide</a>.</li>
<li><a href="https://github.com/biomejs/biome/blob/main/crates/biome\_parser/CONTRIBUTING.md">Help</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_yaml\_parser">building</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_html\_parser">Biome</a> <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_markdown\_parser">parsers</a>!
One interesting fact about Biome parsers is that they are recoverable parsers <a href="https://biomejs.dev/internals/architecture/#parser-and-cst">error resilient</a> which emit a <a href="https://en.wikipedia.org/wiki/Parse\_tree">CST</a> instead of a classic AST.</li>
<li>Implement new capabilities in our <a href="https://github.com/biomejs/biome/tree/main/crates/biome\_lsp">LSP (Language Server Protocol)</a>, or add new features in one of our editor extensions: <a href="https://github.com/biomejs/biome-vscode">VS Code</a>, <a href="https://github.com/biomejs/biome-zed">Zed</a> and <a href="https://github.com/biomejs/biome-intellij">JetBrains IntelliJ</a>.</li>
</ul>
<div><h4 id="financial-help">Financial help</h4></div>
<p>Additionally, the project provides an <a href="https://biomejs.dev/enterprise">enterprise support program </a> where a company you can employ one of the core contributors to work a specific aspect of the Biome toolchain.</p>VS Code extension V3https://biomejs.dev/blog/2025-05-29-biome-vscode-v3/https://biomejs.dev/blog/2025-05-29-biome-vscode-v3/Biome releases v3 of the VS Code extension
Tue, 29 Apr 2025 00:00:00 GMT<p>We’re excited to announce that version 3 of the Biome VS Code extension is now
available! This release includes a range of new features and improvements to
make your development experience even better:</p>
<ul>
<li>🗄️ Support for multi-root workspaces</li>
<li>📝 Support for single-file mode</li>
<li>👻 Support for unsaved files</li>
<li>🔄 Automatic reload after updating Biome</li>
<li>⚙️ Automatic reload after configuration changes</li>
<li>✨ Improved status indicator</li>
</ul>
<div><h2 id="multi-root-workspaces">Multi-root workspaces</h2></div>
<p>The Biome extension now supports <a href="https://code.visualstudio.com/docs/editor/multi-root-workspaces">multi-root workspaces</a>, so you can work on
multiple projects side by side in a single VS Code window. Each workspace folder
now runs its own independent Biome instance, keeping your projects isolated.</p>
<p>:::caution[heads up for pre-release users] If you’ve been using the pre-release
version over the past few months, please note that support for the
<code dir="auto">biome.projects</code> setting has been <strong>removed</strong> in the final release. We now
recommend using <strong>multiple workspace folders</strong> instead to manage multiple
projects. :::</p>
<div><h2 id="single-file-mode">Single-file mode</h2></div>
<p>Sometimes you just need to make a quick edit to <em>that one file</em>. The extension
now fully supports <strong>single-file mode</strong>, making it easy to work with files that
aren’t part of a full project.</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>code</span><span> </span><span>that-one-file.js</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>To use this feature, make sure you have <a href="https://biomejs.dev/guides/manual-installation/">Biome installed globally</a>. No worries
if you forget, the extension will let you know if it can’t find Biome in your
<code dir="auto">PATH</code>.</p>
<div><h2 id="unsaved-files--vs-code-settings">Unsaved files &#x26; VS Code settings</h2></div>
<p>The extension now supports formatting and linting unsaved (Untitled) files, as
well as your VS Code settings. When you open one of these, the extension will
spin up a global Biome instance on demand.</p>
<p>As with single-file mode, this feature requires <a href="https://biomejs.dev/guides/manual-installation/">Biome to be installed
globally</a>. The extension will notify you if it’s missing from your PATH.</p>
<div><h2 id="automatic-reload">Automatic reload</h2></div>
<p>When the extension detects that Biome has been updated in your project
dependencies, it will automatically reload the relevant Biome instances to use
the latest version.</p>
<p>Additionally, any changes to the extension’s configuration will trigger a reload
of the Biome instance to ensure your new settings take effect immediately.</p>
<div><h2 id="improved-status-indicator">Improved status indicator</h2></div>
<p>The status bar now more reliably reflects the status of Biome for your active
workspace folder. When you switch between workspace folders, the indicator
updates accordingly.</p>
<p>Plus, clicking the status indicator opens the logs for the current Biome
instance, making it easier to access logs when troubleshooting.</p>
<div><h2 id="retiring-the-downloader">Retiring the downloader</h2></div>
<p>From the start, the downloader was meant to bridge the gap until you installed
Biome as a project dependency.</p>
<p>Managing the lifecycle of downloaded binaries—including updates and
cross-platform support is complex. We believe package managers handle this
better than we could.</p>
<p>Going forward, if the extension needs a global Biome installation but can’t find
it, you’ll see a notification with instructions on how to install Biome
globally. And don’t worry, you can easily silence this notification if you
Wed, 02 Apr 2025 00:00:00 GMT<p>Back at the start of 2024, Biome added an ambitious goal to its
<a href="https://biomejs.dev/blog/roadmap-2024">roadmap</a>: integrate a subset of the
<strong>TypeScript type system</strong> directly into Biome so that type-informed lint rules
can work out of the box.</p>
<p>In order to make this feasible, we first needed better infrastructure. The main
blocker for this was multi-file analysis, which is coming with
<a href="https://biomejs.dev/blog/biome-v2-0-beta">Biome 2.0</a>.</p>
<p>Today, we finally have the technical means to implement this goal, but, as a
project, we need more than only technical means. Which is why we are grateful
to announce Vercel as a partner to help us achieve this goal and push the web
forward.</p>
<p><a href="https://vercel.com/">Vercel</a> has contracted me (one of the Biome lead
developers) to work on our type inference effort for many months. Vercel’s goal
with this partnership is to both help improve their own internal linter DX (as
they have recently standardized on Biome) and share those improvements with the
rest of the JavaScript ecosystem.</p>
<p>We aim to have a fully
functioning<a href="#how-can-you-write-a-type-informed-lint-rule-if-you-dont-know-the-type-information-is-correct">(\*)</a>
versions of the <a href="https://next.biomejs.dev/linter/rules/no-floating-promises/"><code dir="auto">noFloatingPromises</code></a>
rule and a similar <code dir="auto">noMisusedPromises</code> rule.</p>
<div><h2 id="frequently-asked-questions">Frequently Asked Questions</h2></div>
<p>Because type inference and type checkers are popular topics in our community,
I have collected a few common questions on this topic.</p>
<div><h3 id="are-you-reimplementing-a-type-checker-in-biome">Are you reimplementing a type checker in Biome?</h3></div>
<p>No. TypeScript’s <code dir="auto">tsc</code> is a complex and fully-featured type checker, and we have
no intention to rebuild it. For type <em>checking</em> you are expected to continue to
use <code dir="auto">tsc</code>.</p>
<p>This work focuses on type <em>inference</em> which is a small subset of the
functionality of a full type checker. The goal is to be able to write lint rules
that act on type information, without needing to prove that this type
information is correct.</p>
<div><h3 id="how-can-you-write-a-type-informed-lint-rule-if-you-dont-know-the-type-information-is-correct">How can you write a type-informed lint rule if you don’t know the type information is correct?</h3></div>
<p>Linters have different aims than type checkers. Where a type checker aims to
detect misuse of types, a linter aims to detect common mistakes in general. But
the goal of detecting common mistakes doesn’t require 100% correctness when it
comes to the types it operates on. In fact, even the
<a href="https://github.com/Microsoft/TypeScript/wiki/TypeScript-Design-Goals">TypeScript Design Goals</a>
state they are willing to compromise correctness in favor of productivity.</p>
<p>For a linter, what’s most important is that we don’t flag <em>false positives</em>,
instances where our lint rules may think there’s an issue when really there’s
not. False positives are a source of frustration for developers, because they
take time to analyze; time that was wasted when it turns out there really wasn’t
an issue to begin with.</p>
<p>On the other hand, <em>false negatives</em> are less problematic. They represent
situations where we wish the lint rule would flag an issue, but didn’t. They can
also represent lost productivity (by not flagging the issue early in the
pipeline), but they are not productivity lost due to the rule itself.</p>
<p>Hypothetically, a lint rule that has no false positives, but has 20% false
negatives, still offers 80% of the value of a rule that is always correct. So
our goal is simply: Create lint rules that don’t flag false positives,
while trying to get the amount of false negatives down as much as we can.</p>
<p>We cannot say upfront which percentage we will actually achieve, but since
Vercel is sponsoring this work, we’ll use their repositories as a benchmark and
try to optimise towards their use cases.</p>
<div><h3 id="how-does-microsofts-announcement-of-a-go-port-for-tsc-influence-your-work">How does Microsoft’s announcement of a Go port for <code dir="auto">tsc</code> influence your work?</h3></div>
<p>It’s too early to tell. The Go port is not available to users yet, and the APIs
that should allow it to be used by other tooling aren’t expected until the end
of the year. Additionally, even though the Go port is supposedly much faster
than the Node.js version, it will likely still be significantly slower than an
implementation built into Biome’s core due to inter-process communication and
the need to do duplicate work such as parsing files in separate processes.</p>
<p>For now, that gives us an opportunity to pursue our own type inference
implementation and see how it goes. When the Go version is available for
integration into other tools, we can always reevaluate our approach.</p>
<div><h3 id="can-we-follow-your-progress">Can we follow your progress?</h3></div>
<p>Yes! There’s a public project overview that people can inspect:
<a href="https://github.com/orgs/biomejs/projects/4/views/2">https://github.com/orgs/biomejs/projects/4/views/2</a></p>
<p>Note that issues may be continuously added to the project as false negatives
keep popping up.</p>Biome v2.0 betahttps://biomejs.dev/blog/biome-v2-0-beta/https://biomejs.dev/blog/biome-v2-0-beta/Biome 2.0 will be packed with major features and many smaller fixes, rules, and other improvements.
There's a lot to unpack, and we request the community's help testing this beta, so the final
release can be as smooth as possible.
Mon, 24 Mar 2025 00:00:00 GMT<p>After hard work from our team, Biome’s long-awaited 2.0 release is nearing completion. It will be packed with many large features, so we would like your help testing it with a public beta!</p>
<p>If you would like to try it out, you can update Biome and migrate your configuration using the following commands:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@beta</span></div></div><div><div><span>npx</span><span> </span><span>@biomejs/biome@beta</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Also, make sure you use the prereleases of our IDE extensions. The stable versions of our extensions are not yet prepared for Biome 2.0!</p>
<p>Documentation for the upcoming release can be found at <a href="https://next.biomejs.dev/">https://next.biomejs.dev/</a>.</p>
<div><h2 id="new-features">New features</h2></div>
<p>While the final 2.0 release may still have small changes in its final feature set, here’s what you can expect in the beta:</p>
<ul>
<li><strong>Plugins:</strong> You can write custom lint rules using GritQL.</li>
<li><strong>Domains:</strong> Domains help to group lint rules by technology, framework, or well, domain. Thanks to domains, your default set of recommended lint rules will only include those that are relevant to your project.</li>
<li><strong>Multi-file analysis:</strong> Lint rules can now apply analysis based on information from other files, enabling rules such as <code dir="auto">noImportCycles</code>.</li>
<li><strong><code dir="auto">noFloatingPromises</code>:</strong> Still a proof-of-concept, but our first type-aware lint rule is making an appearance.</li>
<li>Our <strong>Import Organizer</strong> has seen a major revamp.</li>
<li><strong>Assists:</strong> Biome Assist can provide actions without diagnostics, such as sorting object keys.</li>
<li><strong>Improved suppressions:</strong> Suppress a rule in an entire file using <code dir="auto">// biome-ignore-all</code>, or suppress a range using <code dir="auto">// biome-ignore-start</code> and <code dir="auto">// biome-ignore-end</code>.</li>
<li><strong>HTML formatter:</strong> Still in preview, this is the first time we ship an HTML formatter.</li>
<li>Many, <strong>many</strong>, fixes, new lint rules, and other improvements.</li>
</ul>
<div><h3 id="plugins">Plugins</h3></div>
<p>Biome 2.0 comes with our first iteration of <a href="https://biomejs.dev/linter/plugins">Linter Plugins</a>.</p>
<p>These plugins are still limited in scope: They allow for matching code snippets and reporting diagnostics on them.</p>
<p>Here is an example of a plugin that reports on all usages of <code dir="auto">Object.assign()</code>:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>`$fn($args)` where {</span></div></div><div><div><span><span> </span></span><span>$fn &#x3C;: `Object.assign`,</span></div></div><div><div><span><span> </span></span><span>register\_diagnostic(</span></div></div><div><div><span><span> </span></span><span>span = $fn,</span></div></div><div><div><span><span> </span></span><span>message = "Prefer object spread instead of `Object.assign()`"</span></div></div><div><div><span><span> </span></span><span>)</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>It’s a first step, but we have plenty of ideas for making them more powerful, and we’ll eagerly hear from our users on what they would like to see prioritised.</p>
<div><h3 id="domains">Domains</h3></div>
<p>We’ve introduced a new linter feature: <a href="https://next.biomejs.dev/linter/domains/">Domains</a>.</p>
<p>Domains are a new way to organise lint rules by technology, framework, or well, domain. Right now, we have identified four domains:</p>
<ul>
<li><code dir="auto">next</code>: Rules related to Next.js.</li>
<li><code dir="auto">react</code>: Rules related to React.</li>
<li><code dir="auto">solid</code>: Rules related to Solid.js.</li>
<li><code dir="auto">test</code>: Rules related to testing, regardless of framework or library.</li>
</ul>
<p>You can enable and disable rules that belong to a domain together:</p>
<div><figure><figcaption><span>biome.jsonc</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"</span><span>linter</span><span>"</span><span>: {</span></div></div><div><div><span> </span><span>"</span><span>domains</span><span>"</span><span>: {</span></div></div><div><div><span> </span><span>"</span><span>test</span><span>"</span><span>: </span><span>"</span><span>all</span><span>"</span><span>, </span><span>// all rules that belong to this domain are enabled</span></div></div><div><div><span> </span><span>"</span><span>react</span><span>"</span><span>: </span><span>"</span><span>recommended</span><span>"</span><span>, </span><span>// only the recommended rules from this domain are enabled</span></div></div><div><div><span> </span><span>"</span><span>solid</span><span>"</span><span>: </span><span>"</span><span>none</span><span>"</span><span> </span><span>//</span><span> </span><span>rules</span><span> </span><span>related</span><span> </span><span>to</span><span> </span><span>Solid</span><span> </span><span>are</span><span> </span><span>disabled</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>But it gets better: Biome will automatically inspect your <code dir="auto">package.json</code> and determine which domains should be enabled by default. For instance, if you have <code dir="auto">react</code> defined as one of your dependencies, the default setting for the <code dir="auto">react</code> domain automatically becomes <code dir="auto">recommended</code>.</p>
<p>This way, Biome’s total set of recommended rules should be most relevant to your specific project needs.</p>
<p>And finally, domains can add global variables to the <code dir="auto">javascript.globals</code> setting. This should make Biome even easier to setup.</p>
<div><h3 id="multi-file-analysis">Multi-file analysis</h3></div>
<p>Before version 2.0, Biome lint rules could only operate on one file at a time. This brought us far, but many of the more interesting rules require information from other files too.</p>
<p>To accomplish this, we have added a <em>file scanner</em> to Biome that scans all the files in your project and indexes them, similar to what an LSP service might do in your IDE. We’re not going to beat around the bush: Scanning projects means that Biome has become slower for many projects. But we do believe the ability to do multi-file analysis is worth it. And without a scanner, multi-file analysis would become <em>even slower</em>, as rules would need to perform ad-hoc file system access individually.</p>
<p>That said, this is a beta, and there are certainly more opportunities to improve our scanner and its performance. If you have a repository where you feel our performance became unacceptably slow, please reach out and <a href="https://github.com/biomejs/biome/issues/new?template=03\_bug.yml">file an issue</a>.</p>
<p>For now, we have a few interesting rules that can make use of our multi-file analysis:</p>
<ul>
<li><a href="https://next.biomejs.dev/linter/rules/no-import-cycles/"><code dir="auto">noImportCycles</code></a> is able to look at import statements and detect cycles between them.</li>
<li><a href="https://next.biomejs.dev/linter/rules/no-private-imports/"><code dir="auto">noPrivateImports</code></a> is a new rule based on the <code dir="auto">useImportRestrictions</code> nursery rule from Biome 1.x, and inspired by ESLint’s <a href="https://github.com/uhyo/eslint-plugin-import-access"><code dir="auto">plugin-import-access</code></a>. It forbids importing symbols with an <code dir="auto">@private</code> JSDoc tag from other modules, and forbids importing symbols with an <code dir="auto">@package</code> tag if the importing file is not in the same folder or one of its subfolders.</li>
<li><a href="https://next.biomejs.dev/linter/rules/use-import-extensions/"><code dir="auto">useImportExtensions</code></a> has been improved because it can now determine the actual extension that needs to be used for an import, instead of guessing based on heuristics.</li>
</ul>
<p>Finally, we’ve also designed the multi-file analysis with monorepos in mind. While full monorepo support may not make it in time for the 2.0 release, we expect to be able to deliver more on this front soon.</p>
<div><h3 id="nofloatingpromises"><code dir="auto">noFloatingPromises</code></h3></div>
<p>With Biome’s linter we have always strived to provide a battery-included approach to linting. This means we’re not just aiming to replace ESLint, but also its plugins. One of the hardest plugins to replace is <strong><code dir="auto">typescript-eslint</code></strong>.</p>
<p>Biome has featured some rules from <code dir="auto">typescript-eslint</code> for a while now, but we could never replace all rules, because they relied on type information for their analysis. And in order to get type information, <code dir="auto">typescript-eslint</code> relies on <code dir="auto">tsc</code> itself, which is rather slow and also complicates setup.</p>
<p>This is about to change. With Biome 2.0, we’re introducing a first version of the <a href="https://next.biomejs.dev/linter/rules/no-floating-promises"><code dir="auto">noFloatingPromises</code></a> rule, one of the most-requested rules that relies on type information. In fairness, we should not consider it more than a proof-of-concept right now, because there are some notable limitations to its capabilities:</p>
<ul>
<li>It doesn’t understand complex types yet.</li>
<li>It cannot do type inference yet.</li>
<li>It can currently only analyse types that occur in the same file.</li>
</ul>
<p>Still, its capabilities are sufficient to catch some of the low-hanging fruit. Consider this small snippet:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>async</span><span> </span><span>function</span><span> </span><span>returnsPromise</span><span>()</span><span> { </span><span>/\* ... \*/</span><span> }</span></div></div><div><div>
</div></div><div><div><span>returnsPromise</span><span>()</span><span>.</span><span>then</span><span>(</span><span>()</span><span> </span><span>=></span><span> {});</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>It will trigger the following diagnostic:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>example.js:3:1 lint/nursery/noFloatingPromises ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span></div></div><div><div>
</div></div><div><div><span><span> </span></span><span>ℹ A “floating” Promise was found, meaning it is not properly handled and could lead to ignored errors or unexpected behavior.</span></div></div><div><div>
</div></div><div><div><span><span> </span></span><span>1 │ async function returnsPromise() { /\* ... \*/ }</span></div></div><div><div><span><span> </span></span><span>2 │</span></div></div><div><div><span><span> </span></span><span>> 3 │ returnsPromise().then(() => {});</span></div></div><div><div><span><span> </span></span><span>│ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</span></div></div><div><div><span><span> </span></span><span>5 │</span></div></div><div><div>
</div></div><div><div><span><span> </span></span><span>ℹ This happens when a Promise is not awaited, lacks a .catch or .then rejection handler, or is not explicitly ignored using the void operator.</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>As you can guess, we intend to expand this rule’s capabilities over time. And with our new multi-file analysis in place, we expect to be able to make serious strides with this. Stay tuned for more announcements on this front!</p>
<div><h3 id="import-organizer-revamp">Import Organizer Revamp</h3></div>
<p>In Biome 1.x, our Import Organizer had several limitations:</p>
<ul>
<li>
<p>Groups of imports or exports would be considered separate <em>chunks</em>, meaning they would be sorted independently. This meant the following <strong>didn’t work</strong> as expected:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>It would correctly sort <code dir="auto">"library1"</code> to be placed above <code dir="auto">"./utils.js"</code>, but it wouldn’t be able to
carry it over the newline to the top. What we got was this:</p>
<div><figure><figcaption><span>organizer\_v1.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>But instead, what we really wanted was this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { lib2 } </span><span>from</span><span> </span><span>"</span><span>library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { util } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>Separate imports from the same module wouldn’t be merged. Consider the following example:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> { util1 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { util2 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Nothing would be done to merge these import statements, whereas what we would have wanted was this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { util1, util2 } </span><span>from</span><span> </span><span>"</span><span>./utils.js</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>No custom ordering could be configured. Maybe you didn’t really like the default approach of ordering by “distance” from the source file that you’re importing from. Maybe you wanted to organise like this:</p>
<div><figure><figcaption><span>organizer\_v2.js</span></figcaption><pre><code><div><div><span>import</span><span> { open } </span><span>from</span><span> </span><span>"</span><span>node:fs</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { internalLib1 } </span><span>from</span><span> </span><span>"</span><span>@company/library1</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> { internalLib2 } </span><span>from</span><span> </span><span>"</span><span>@company/library2</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>import</span><span> { lib1 } </span><span>from</span><span> </span><span>"</span><span>library1</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
</ul>
<p>In Biome 2.0, all these limitations are lifted. In fact, if you look at the examples above, all snippets labeled <code dir="auto">organizer\_v2.js</code> can be produced just like that by our new import organizer.</p>
<p>Other improvements include support for organizing <code dir="auto">export</code> statements, support for “detached” comments for explicitly separating import chunks if necessary, and import attribute sorting.</p>
<p>You can find the documentation on the new import organizer at <a href="https://next.biomejs.dev/assist/actions/organize-imports/">https://next.biomejs.dev/assist/actions/organize-imports/</a>.</p>
<div><h3 id="assists">Assists</h3></div>
<p>The Import Organizer was always a bit of a special case in Biome. It was neither part of the linter, nor of the formatter. This was because we didn’t want it to show diagnostics the way the linter does, while its organizing features went beyond what we expect from the formatter.</p>
<p>In Biome 2.0, we have generalised such use cases in the form of Biome Assist. The assist is meant to provide <strong>actions</strong>, which are similar to the <em>fixes</em> in lint rules, but without the diagnostics.</p>
<p>The Import Organizer has become an assist, but we’ve started using this approach for new assists too: <a href="https://next.biomejs.dev/assist/actions/use-sorted-keys/"><code dir="auto">useSortedKeys</code></a> can sort keys in object literals, while <a href="https://next.biomejs.dev/assist/actions/use-sorted-attributes/"><code dir="auto">useSortedAttributes</code></a> can sort attributes in JSX.</p>
<p>For more information about assists, see: <a href="https://next.biomejs.dev/assist/">https://next.biomejs.dev/assist/</a></p>
<div><h3 id="improved-suppressions">Improved suppressions</h3></div>
<p>In addition to the <code dir="auto">// biome-ignore</code> comments we already supported, we now support <code dir="auto">// biome-ignore-all</code> for suppressing a lint rule or the formatter in an entire file.</p>
<p>We also added support for suppression ranges using <code dir="auto">// biome-ignore-start</code> and <code dir="auto">// biome-ignore-end</code>. Note that <code dir="auto">// biome-ignore-end</code> is optional in case you want to let a range run until the end of the file.</p>
<p>For more information about suppressions, see: <a href="https://next.biomejs.dev/linter/#suppress-lint-rules">https://next.biomejs.dev/linter/#suppress-lint-rules</a></p>
<div><h3 id="html-formatter">HTML formatter</h3></div>
<p>After a few months of hard work, we are happy to announce that the HTML formatter is now ready for users to try out and start reporting bugs! This is a huge step towards Biome fully supporting HTML-ish templating languages used in frameworks like Vue and Svelte.</p>
<p>The HTML formatter only touches actual <code dir="auto">.html</code> files for now, so no formatting of html in <code dir="auto">.vue</code> or <code dir="auto">.svelte</code> files yet. It also won’t format embedded languages like JavaScript or CSS yet. HTML’s options like <code dir="auto">attributePosition</code>, <code dir="auto">bracketSameLine</code>, and <code dir="auto">whitespaceSensitivity</code> have been implemented.</p>
<p>The HTML formatter is still pretty experimental, so it will remain <strong>disabled by default for the full 2.0 release</strong>. At the time of writing, Biome is able to parse the grand majority of Prettier’s HTML tests, and format 46/124 of them correctly. Despite not matching Prettier yet, we’re pretty confident that it <em>should</em> output documents that are formatted adequately without destroying anything. If you find a case where it doesn’t, <a href="https://github.com/biomejs/biome/issues">please let us know</a>!</p>
<p>You can enable the HTML formatter by adding the following to your config file:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"html"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="new-rules">New rules</h3></div>
<p>Several new rules have added since v1.9:</p>
<ul>
<li><a href="https://next.biomejs.dev/linter/rules/no-await-in-loop"><code dir="auto">noAwaitInLoop</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-bitwise-operators/"><code dir="auto">noBitwiseOperators</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-destructured-props/"><code dir="auto">noDestructuredProps</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-floating-promises"><code dir="auto">noFloatingPromises</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-import-cycles"><code dir="auto">noImportCycles</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-private-imports/"><code dir="auto">noPrivateImports</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-ts-ignore"><code dir="auto">noTsIgnore</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/no-unwanted-polyfillio"><code dir="auto">noUnwantedPolyfillio</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/use-consistent-object-definition/"><code dir="auto">useConsistentObjectDefinition</code></a></li>
<li><a href="https://next.biomejs.dev/linter/rules/use-for-component/"><code dir="auto">useForComponent</code></a></li>
</ul>
<div><h3 id="miscellaneous">Miscellaneous</h3></div>
<ul>
<li><strong>BREAKING:</strong> The configuration fields <code dir="auto">include</code> and <code dir="auto">ignore</code> have been replaced with a single <code dir="auto">includes</code> field.</li>
<li><strong>BREAKING:</strong> Reworked some recommended rules recommended to be less pedantic and blocking. This is a breaking change if your project relied on those rules to block the CI in case of violations. If you used the <code dir="auto">migrate</code> command, the behaviour should remain as before.</li>
<li><strong>BREAKING:</strong> The <code dir="auto">style</code> rules aren’t recommended anymore. If you used the <code dir="auto">migrate</code> command, the behaviour should remain as before.</li>
<li><strong>BREAKING:</strong> Removed deprecated rules:
<ul>
<li><code dir="auto">noConsoleLog</code></li>
<li><code dir="auto">noInvalidNewBuiltin</code></li>
<li><code dir="auto">noNewSymbol</code></li>
<li><code dir="auto">useShorthandArrayType</code></li>
<li><code dir="auto">useSingleCaseStatement</code></li>
</ul>
</li>
<li><strong>BREAKING:</strong> Many deprecated options, including some that still referenced the old Rome name, have been removed.</li>
<li>Added a new option <code dir="auto">javascript.parser.jsxEverywhere</code> to control whether Biome should expect JSX syntax in <code dir="auto">.js</code>/<code dir="auto">.mjs</code>/<code dir="auto">.cjs</code> files.</li>
<li>Improved monorepo support: The rule <a href="https://biomejs.dev/linter/rules/no-undeclared-dependencies/"><code dir="auto">noUndeclaredDependencies</code></a> now works correctly in monorepos by using the nearest <code dir="auto">package.json</code> file, instead of only the root one.</li>
<li>We have enabled support for <code dir="auto">.editorconfig</code> files by default.</li>
<li>Changed default formatting of <code dir="auto">package.json</code> to align better with formatting by package managers.</li>
</ul>
<div><h3 id="and-more">And more!</h3></div>
<p>For the full list of changes, please refer to our <a href="https://biomejs.dev/internals/changelog/">changelog</a>.</p>Roadmap 2025 and Biome 2.0https://biomejs.dev/blog/roadmap-2025/https://biomejs.dev/blog/roadmap-2025/A look at what 2025 will bring for us: Biome 2.0, enterprise support, and our roadmap
Wed, 22 Jan 2025 00:00:00 GMT<p>Today we’re happy to share our plans for Biome 2.0 as well as the rest of our roadmap for 2025. But before we dive into what’s coming, let’s do a quick recap of the major developments in 2024.</p>
<div><h2 id="-recap-biome-in-2024">🎆 Recap: Biome in 2024</h2></div>
<p>2024 was a great year for Biome. Let’s see what happened:</p>
<ul>
<li>We released 4 new “minor” Biome versions, from 1.6 through 1.9, with plenty of useful features:
<ul>
<li>New <code dir="auto">biome search</code> and <code dir="auto">biome explain</code> commands, while the <code dir="auto">biome migrate</code> command was significantly expanded to help users coming from ESLint and Prettier.</li>
<li>Added support for <strong>CSS</strong> and <strong>GraphQL</strong> formatting and linting.</li>
<li>Partial support for <strong>Astro</strong>, <strong>Svelte</strong> and <strong>Vue</strong> files.</li>
<li>The ability to let configuration files extend from one another, which is especially useful in monorepo and larger organizational setups.</li>
<li>Custom <a href="https://biomejs.dev/reference/reporters/">reporters</a> for better CI integration and machine-readable output.</li>
<li>Support for <code dir="auto">.editorconfig</code>.</li>
<li>We added countless new lint rules and miscellaneous fixes and improvements, with a special shoutout to <a href="https://biomejs.dev/linter/rules/use-sorted-classes/"><code dir="auto">useSortedClasses</code></a> that marks the beginning of dedicated <strong>Tailwind</strong> support.</li>
</ul>
</li>
<li>Our <a href="https://github.com/biomejs/biome/blob/main/CONTRIBUTING.md#current-members">team of maintainers</a> has grown from 10 members at the start of 2024 to 18 today.</li>
<li>We won the <strong>Productivity Booster</strong> award of the <a href="https://osawards.com/javascript/2024">OS Awards 2024</a>.</li>
<li>We gained several new <a href="https://github.com/biomejs/biome#sponsors">sponsors</a>.</li>
<li>We improved our IDE support on multiple fronts:
<ul>
<li>A new Zed extension has been contributed to the project.</li>
<li>Our VS Code extension has seen an overhaul that’s currently in Pre-Release.</li>
<li>And even though this happened after the new year, we shouldn’t neglect to mention that our IDEA plugin has seen a major update too, which is now available in the nightly channel.</li>
</ul>
</li>
</ul>
<div><h2 id="-enterprise-support">💳 Enterprise Support</h2></div>
<p>One more thing that we are happy to announce is that as of January 2025, we are also offering <a href="https://biomejs.dev/enterprise">Enterprise Support</a> for Biome. Hopefully this will allow some of our contributors to spend more of their time and effort towards Biome!</p>
<div><h2 id="️-biome-20">⏭️ Biome 2.0</h2></div>
<p>Right now our team is busy preparing for the Biome 2.0 release. Because our project is still run by volunteer contributors, we do not have an ETA for you. But we can share some of the goodies that will be coming:</p>
<ul>
<li><strong>Plugins</strong>. A long-requested feature, we started the development of Biome plugins after an <a href="https://github.com/biomejs/biome/discussions/1762">RFC process</a> that started in January 2024. Biome 2.0 will feature the first fruits of this labor: Users will be able to create their own lint rules using <a href="https://docs.grit.io/language/overview">GritQL</a>.</li>
<li><strong>Domains</strong>. <a href="https://github.com/biomejs/biome/blob/main/.changeset/introduce\_the\_domains\_linter\_feature.md">Domains</a> are a configuration feature that makes it easy for users to enable or disable all rules related to a specific domain, such as React, Next.js or testing frameworks. It also allows Biome to automatically enable recommended domain-specific rules based on the dependencies listed in your <code dir="auto">package.json</code>.</li>
<li><strong>Monorepo Support</strong>. While support for monorepos was already improved with our <code dir="auto">extends</code> feature in <code dir="auto">biome.json</code>, many weak spots remained. Biome 2.0 has an improved architecture based on an internal <code dir="auto">ProjectLayout</code> that should resolve most of these.</li>
<li><strong>Suppressions</strong>. Biome already allowed <em>suppression</em> of linter diagnostics through the use of <code dir="auto">// biome-ignore</code> suppression comments. With Biome 2.0 we’re adding support for <code dir="auto">// biome-ignore-all</code> and <code dir="auto">// biome-ignore-start</code>/<code dir="auto">biome-ignore-end</code> comments.</li>
<li><strong>Multi-file analysis</strong>. Last but not least, we’re adding true <a href="https://github.com/biomejs/biome/issues/3307">Multi-file support</a> to Biome 2.0. This means that our lint rules will be able to query information from other files, which will enable much more powerful lint rules.</li>
</ul>
<div><h2 id="-2025-roadmap">🌌 2025 roadmap</h2></div>
<p>Again, we should preface a disclaimer here: We’re a community-driven project, so we cannot promise to deliver any of the features below. But that doesn’t mean we don’t have a wishlist of things we would like to work on in 2025 😉</p>
<p>This year we will focus on:</p>
<ul>
<li><a href="https://github.com/biomejs/biome/issues/4726"><strong>HTML support</strong></a>. No toolchain for the web is complete without it, and we’re already working on it!</li>
<li><a href="https://github.com/biomejs/biome/issues/3334"><strong>Embedded languages</strong></a>. CSS or GraphQL snippets inside a template literal in a JavaScript file? JavaScript or CSS inside an HTML file? Biome should be able to handle these as well, and we’ll try to make it happen. This should also lead to better support for <strong>Astro</strong>, <strong>Svelte</strong>, and <strong>Vue</strong> than we have today.</li>
<li><a href="https://github.com/biomejs/biome/issues/3187"><strong>Type inference</strong></a>. This was already a wish for 2024, and we’re busy filling in the prerequisites such as multi-file analysis. There’s even an <a href="https://github.com/biomejs/biome/pull/4911">early proof-of-concept</a> for a <code dir="auto">noFloatingPromises</code> rule. This year we want to ship a real version of <code dir="auto">noFloatingPromises</code>, and hopefully dabble further into type inference.</li>
<li><strong>.d.ts generation</strong>. While we’re on the subject of types, we would also like to create our first transformation: generating <code dir="auto">.d.ts</code> files from TypeScript sources. Initially we would only focus on TypeScript using <a href="https://www.typescriptlang.org/tsconfig/#isolatedModules">Isolated Modules</a>.</li>
<li><strong>JSDoc support</strong>. Can we use <a href="https://jsdoc.app/">JSDoc</a> comments as a source of type information too? If we are able to do type inference, this seems an opportunity we cannot pass on.</li>
<li><strong>Markdown support</strong>. Some work <a href="https://github.com/biomejs/biome/issues/3718">has already started</a> for it and it would be a nice addition to round out our language support.</li>
<li><strong>More plugins</strong>. While Biome 2.0 will launch with the ability to create lint rules in GritQL, that’s only the tip of the iceberg. We know our users want more, and we certainly have ideas for more types of plugins. We’ll first collect feedback from the 2.0 release, and then we’ll decide which plugin area we’ll focus on next.</li>
</ul>
<div><h2 id="️-your-support">❤️ Your Support</h2></div>
<p>We would like to thank our users and sponsors alike for their amazing support in 2024! Without you, this project would not be what it is today.</p>
<p>Hopefully we can also count on your support for the coming year. If you would like to help out, you can:</p>
<ul>
<li><a href="https://github.com/biomejs/biome/blob/main/CONTRIBUTING.md">Become a contributor</a>. Please help us to build those features!</li>
<li><a href="https://github.com/biomejs/website/">Improve our documentation</a>. Write guides or recipes, or help to keep our translations up-to-date for non-English speakers.</li>
</ul>Biome v1.9 Anniversary Releasehttps://biomejs.dev/blog/biome-v1-9/https://biomejs.dev/blog/biome-v1-9/Let's celebrate the first anniversary of Biome and the release of Biome v1.9.
This new version enables CSS and GraphQL formatting and linting by default.
It also brings .editorconfig support and introduces a new search command.
Thu, 12 Sep 2024 00:00:00 GMT<p>Today we’re excited to announce the release of Biome v1.9 and to celebrate the first anniversary of Biome 🎊 Let’s take a look back at the first year of Biome and then explore the new features in Biome 1.9.</p>
<div><h2 id="one-year-of-biome">One year of Biome</h2></div>
<p>We officially <a href="https://biomejs.dev/blog/annoucing-biome/">announced Biome</a> on 29 August 2023. From its inception, Biome has been a free open source software driven by its community. We have a <a href="https://github.com/biomejs/biome/blob/main/GOVERNANCE.md">governance</a> and a solid base of contributors to ensure the longevity of the project.</p>
<p>In October 2023, one of the creators of <a href="https://prettier.io/">Prettier</a> launched <a href="https://console.algora.io/challenges/prettier">the Prettier challenge</a> that rewarded any project written in Rust that passes at least 95% of the Prettier tests for JavaScript. The aim of this challenge was to create a fast competitor to Prettier in order to stimulate improvements in Prettier’s performance. We quickly organized ourselves to get there as soon as possible. By the end of November, we <a href="https://biomejs.dev/blog/biome-wins-prettier-challenge/">surpassed this goal</a> by passing 97% of the Prettier tests for JavaScript, as well as TypeScript, JSX and TSX!
The Biome formatter is really fast: it can format a large code base in less than 1 second. In the process, we identified several formatting issues in Prettier. This has also pushed contributions to Prettier that greatly improved its performance. This challenge was a win for the whole web ecosystem!</p>
<p>By winning the challenge, we brought Biome to light. Many developers were excited to discover a fast alternative to Prettier, but also a fast alternative to <a href="https://eslint.org/">ESLint</a>!
The approach of bundling both a formatter and a linter in one tool provides a unified and consistent experience with minimal configuration. Biome has been quickly adopted by many projects, including big ones such as <a href="https://ant.design/">Ant Design</a>, <a href="https://astro.build/">Astro</a>, <a href="https://sentry.io/">Sentry</a>, <a href="https://daisyui.com/">daisyUI</a>, <a href="https://refine.dev/">Refine</a>, <a href="https://discord.com/">Discord</a>, <a href="https://www.pulumi.com/">Pulumi</a>, <a href="https://labelstud.io/">Label Studio</a>, <a href="https://spicetify.app/">Spicetify</a>, <a href="https://apify.com/">Apify</a>, <a href="https://slint.dev/">Slint</a>, <a href="https://rspack.dev/">Rspack</a>, <a href="https://fluidframework.com/">FluidFramework</a>, <a href="https://sourcegraph.com/search?q=file:biome.json&#x26;patternType=literal&#x26;sm=0">and others</a>. Biome surpassed 2.7 million monthly NPM downloads in August 2024.</p>
<p><img alt="Biome monthly NPM downloads" loading="lazy" decoding="async" fetchpriority="auto" width="1062" height="340" src="https://biomejs.dev/\_astro/biome-monthly-npm-downloads.BDqAA5ti\_Z1MJSTe.svg?dpl=69dce24b554af000071740e1"></p>
<p>We also gained many new contributors. Contributors who have made a significant contribution are regularly invited to join the Biome team. We started with a team of 5 core contributors, and we are now a team of <a href="https://github.com/biomejs/biome/blob/main/CONTRIBUTING.md#current-members">8 core contributors and 10 maintainers</a>.</p>
<p>In June 2024, Biome won the <a href="https://osawards.com/javascript/2024">JSNation’s productivity booster Open Source Award</a>.</p>
<div><h2 id="biome-v19">Biome v1.9</h2></div>
<p>As we celebrate Biome’s first year, we’re pleased to announce the release of Biome 1.9, which brings many new features and bug fixes.</p>
<p>Once you have upgraded to Biome v1.9.0, migrate your Biome configuration to the new version by running the <code dir="auto">migrate</code> command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>migrate</span><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="stable-css-formatter-and-linter">Stable CSS formatter and linter</h3></div>
<p>We are thrilled to announce that Biome’s CSS formatter and linter are now considered stable and are <strong>enabled by default</strong>. Do note that Biome only parses <strong>standard CSS syntax</strong> so far, and doesn’t yet handle CSS dialects such as SCSS. As this is brand new functionality, you may also still run into some rough edges. Please report any problems you encounter!</p>
<p>The CSS linter provides 15 stable lint rules that were ported from <a href="https://stylelint.io/">stylelint</a>:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/use-generic-font-names/">a11y/useGenericFontNames</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-direction-in-linear-gradient/">correctness/noInvalidDirectionInLinearGradient</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-grid-areas/">correctness/noInvalidGridAreas</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-position-at-import-rule/">correctness/noInvalidPositionAtImportRule</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-function/">correctness/noUnknownFunction</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-media-feature-name/">correctness/noUnknownMediaFeatureName</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-property/">correctness/noUnknownProperty</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-unit/">correctness/noUnknownUnit</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unmatchable-anb-selector/">correctness/noUnmatchableAnbSelector</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-at-import-rules/">suspicious/noDuplicateAtImportRules</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-font-names/">suspicious/noDuplicateFontNames</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-selectors-keyframe-block/">suspicious/noDuplicateSelectorsKeyframeBlock</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-empty-block/">suspicious/noEmptyBlock</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-important-in-keyframe/">suspicious/noImportantInKeyframe</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-shorthand-property-overrides/">suspicious/noShorthandPropertyOverrides</a></li>
</ul>
<p>It also provides the following nursery lint rules:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-custom-properties/">nursery/noDuplicateCustomProperties</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-irregular-whitespace/">nursery/noIrregularWhitespace</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-pseudo-class/">nursery/noUnknownPseudoClass</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unknown-pseudo-element/">nursery/noUnknownPseudoElement</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-value-at-rule/">nursery/noValueAtRule</a></li>
</ul>
<p>If you don’t want Biome to format and lint your CSS files, you can disable the CSS formatter and linter in the Biome configuration file:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"css"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>false</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>false</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>or on the command line:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--css-formatter-enabled=false</span></div></div><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--css-linter-enabled=false</span></div></div><div><div><span>biome</span><span> </span><span>check</span><span> </span><span>--css-formatter-enabled=false</span><span> </span><span>--css-linter-enabled=false</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Special thanks to <a href="https://github.com/denbezrukov">Denis Bezrukov @denbezrukov</a>, <a href="https://github.com/faultyserver">Jon Egeland @faultyserver</a> and <a href="https://github.com/togami2864">Yoshiaki Togami @togami2864</a> for coordinating and implementing most of the features related to CSS.</p>
<div><h3 id="stable-graphql-formatter-and-linter">Stable GraphQL formatter and linter</h3></div>
<p>Another brand new feature: Biome now formats and lints <a href="https://graphql.org/">GraphQL</a> files by default.</p>
<p>For now, Biome provides only two nursery lint rules:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-fields/">nursery/noDuplicateFields</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-deprecated-reason/">nursery/useDeprecatedReason</a></li>
</ul>
<p>If you don’t want Biome to format and lint your GraphQL files, you can disable the GraphQL formatter and linter in the Biome configuration file:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"graphql"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>false</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>false</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>or on the command line:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--graphql-formatter-enabled=false</span></div></div><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--graphql-linter-enabled=false</span></div></div><div><div><span>biome</span><span> </span><span>check</span><span> </span><span>--graphql-formatter-enabled=false</span><span> </span><span>--css-linter-enabled=false</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Special thanks to <a href="https://www.swan.io/">Swan</a> that funded the implementation of the GraphQL formatter and to <a href="https://github.com/vohoanglong0107">Võ Hoàng Long @vohoanglong0107</a> for implementing most of the features related to GraphQL.</p>
<div><h3 id="search-command">Search command</h3></div>
<p>Back in February, one of our Core Contributors published <a href="https://github.com/biomejs/biome/discussions/1762">a proposal for plugin support</a>. One of the highlights was the use of GritQL as a foundation for our plugin system.</p>
<p><a href="https://docs.grit.io/language/overview">GritQL</a> is a powerful query language that lets you do structural searches on your codebase. This means that trivia such as whitespace or even the type of string quotes used will be ignored in your search query. It also has many features for querying the structure of your code, making it much more elegant for searching code than regular expressions.</p>
<p>Integrating a query language such as GritQL is no easy feat, and throughout the year we published <a href="https://github.com/biomejs/biome/discussions/2286">multiple</a> <a href="https://github.com/biomejs/biome/discussions/2585">status</a> <a href="https://github.com/biomejs/biome/discussions/3392">updates</a>. Today, we release the first product of this effort: A new <code dir="auto">biome search</code> command.</p>
<p>While we believe this command may already be useful to users in some situations (especially when it gets integrated in our IDE extensions!), this command is really a stepping stone towards our plugin efforts. By allowing our users to try it out in a first iteration, we hope to gain insight into the type of queries you want to do, as well as the bugs we need to focus on.</p>
<p>For now, the <code dir="auto">search</code> command is explicitly marked as <strong>EXPERIMENTAL</strong>, since many limitations are yet to be fixed or explored. Keep this in mind when you try it out, and please let us know what you think!
For an overview of specific limitations, please see the <a href="https://github.com/biomejs/biome/issues/2582">dedicated issue</a>.</p>
<p>Even though there are still plenty of limitations, we do believe the integration has progressed far enough that we can shift our focus towards the integration of actual plugins. We cannot yet promise a timeline, but we’ll keep you posted!</p>
<p>PS.: GritQL escapes code snippets using backticks, but most shells interpret backticks as command invocations. To avoid this, it’s best to put single quotes around your Grit queries. For instance, the following command search for all <code dir="auto">console.log</code> invocations:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>search</span><span> </span><span>'</span><span>`console.$method($args)` where { $method &#x3C;: or { `log`, `info` } }</span><span>'</span><span> </span><span>./</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>./benchmark/bench.js:38:3 search ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong>38 │ <span>console.info(`\n⌛ repository: ${name}`);</span></strong>
./packages/@biomejs/js-api/scripts/update-nightly-version.mjs:27:1 search ━━━━━━━━━━━━━━
<strong>27 │ <span>console.log(`version=${version}`);</span></strong>
<span>Searched 67 files in 1034ms. Found 2 matches.</span>
</code></pre>
<p>Special thanks to <a href="https://grit.io">Grit</a> for open-sourcing GritQL, <a href="https://github.com/arendjr">Arend van Beelen @arendjr</a> for integrating the GritQL engine into Biome, and to <a href="https://github.com/BackupMiles/">@BackupMiles</a> for implementing the formatting of search results in the <code dir="auto">biome search</code> command!</p>
<div><h3 id="editorconfig-support"><code dir="auto">.editorconfig</code> support</h3></div>
<p>Biome is now able to take the <a href="https://editorconfig.org/"><code dir="auto">.editorconfig</code></a> of your project into account. This is an opt-in feature. You have to turn it on in your Biome configuration file:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"useEditorconfig"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Note that all options specified in the Biome configuration file override the ones specified in <code dir="auto">.editorconfig</code>. For now, only the <code dir="auto">.editorconfig</code> at the root of your project is taken into account.</p>
<p>Special thanks to <a href="https://github.com/dyc3">Carson McManus @dyc3</a> for implementing this feature!</p>
<div><h3 id="javascript-formatter-and-linter">JavaScript formatter and linter</h3></div>
<p>We updated the JavaScript formatter to match <a href="https://github.com/prettier/prettier/blob/main/CHANGELOG.md#333">Prettier v3.3</a>. The most significant change is adding parentheses around nullish coalescing in ternaries. This change adds clarity to operator precedence.</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>// Input</span></div></div><div><div><span><span>foo</span><span> </span></span><span>?</span><span><span> </span><span>bar</span><span> </span></span><span>??</span><span><span> </span><span>foo</span><span> </span></span><span>:</span><span><span> </span><span>baz</span><span>;</span></span></div></div><div><div>
</div></div><div><div><span>// Biome 1.8.3 and Prettier 3.3.2</span></div></div><div><div><span><span>foo</span><span> </span></span><span>?</span><span><span> </span><span>bar</span><span> </span></span><span>??</span><span><span> </span><span>foo</span><span> </span></span><span>:</span><span><span> </span><span>baz</span><span>;</span></span></div></div><div><div>
</div></div><div><div><span>// Biome 1.9 and Prettier 3.3.3</span></div></div><div><div><span><span>foo</span><span> </span></span><span>?</span><span><span> (</span><span>bar</span><span> </span></span><span>??</span><span><span> </span><span>foo</span><span>) </span></span><span>:</span><span><span> </span><span>baz</span><span>;</span></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Regarding the linter, we stabilized the following lint rules:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-label-without-control/">a11y/noLabelWithoutControl</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-focusable-interactive/">a11y/useFocusableInteractive</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-semantic-elements/">accessibility/useSemanticElements</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-string-concat/">complexity/noUselessStringConcat</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-undefined-initialization/">complexity/noUselessUndefinedInitialization</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-date-now/">complexity/useDateNow</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-undeclared-dependencies/">correctness/noUndeclaredDependencies</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-builtin-instantiation/">correctness/noInvalidBuiltinInstantiation</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unused-function-parameters/">correctness/noUnusedFunctionParameters</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-import-extensions/">correctness/useImportExtensions</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-top-level-regex/">performance/useTopLevelRegex</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-done-callback/">style/noDoneCallback</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-yoda-expression/">style/noYodaExpression</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-consistent-builtin-instantiation/">style/useConsistentBuiltinInstantiation</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-default-switch-clause/">style/useDefaultSwitchClause</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-explicit-length-check/">style/useExplicitLengthCheck</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-throw-new-error/">style/useThrowNewError</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-throw-only-error/">style/useThrowOnlyError</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-console/">suspicious/noConsole</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-evolving-types/">suspicious/noEvolvingTypes</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misplaced-assertion/">suspicious/noMisplacedAssertion</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-react-specific-props/">suspicious/noReactSpecificProps</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-error-message/">suspicious/useErrorMessage</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-number-to-fixed-digits-argument/">suspicious/useNumberToFixedDigitsArgument</a></li>
</ul>
<p>We added the following new rules:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-common-js/">nursery/noCommonJs</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-custom-properties/">nursery/noDuplicateCustomProperties</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-dynamic-namespace-import-access/">nursery/noDynamicNamespaceImportAccess</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-enum/">nursery/noEnum</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-irregular-whitespace">nursery/noIrregularWhitespace</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-restricted-types/">nursery/noRestrictedTypes</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-secrets/">nursery/noSecrets</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-escape-in-regex/">nursery/noUselessEscapeInRegex</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-consistent-member-accessibility/">nursery/useConsistentMemberAccessibility</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-trim-start-end/">nursery/useTrimStartEnd</a></li>
</ul>
<p>And we deprecated the following rules:</p>
<ul>
<li><code dir="auto">correctness/noInvalidNewBuiltin</code>. Use <a href="https://biomejs.dev/linter/rules/no-invalid-builtin-instantiation/">correctness/noInvalidBuiltinInstantiation</a> instead.</li>
<li><code dir="auto">style/useSingleCaseStatement</code>. Use <a href="https://biomejs.dev/linter/rules/no-switch-declarations/">correctness/noSwitchDeclarations</a> instead.</li>
<li><code dir="auto">suspicious/noConsoleLog</code>. Use <a href="https://biomejs.dev/linter/rules/no-console/">suspicious/noConsole</a> instead.</li>
</ul>
<p>Our linter has now more than 250 rules!
Most of the ESLint rules and rules from some plugins have been ported. We are close to completing the port of ESLint.</p>
<div><h3 id="and-more">And more!</h3></div>
<p>For the full list of changes, please refer to our <a href="https://biomejs.dev/internals/changelog/">changelog</a>.</p>
<div><h2 id="whats-next">What’s next</h2></div>
<div><h3 id="vscode-plugin-v3">VSCode plugin v3</h3></div>
<p><a href="https://github.com/nhedger">Nicolas Hedger @nhedger</a> is working on a new version of our first-party VSCode plugin. This new version will improve workspace support and fix some long-standing issues.</p>
<div><h3 id="biome-20">Biome 2.0</h3></div>
<p>During this first year, we have discovered a number of issues that cannot be solved without introducing small breaking changes. For example, we rely on a glob library that sometimes doesn’t behave as users expect. We feel it is time to address these long-standing issues. Following our <a href="https://biomejs.dev/internals/versioning/">versioning philosophy</a>, these small breaking changes cannot be made without releasing a major release. Therefore, the next release of Biome will be a major release: Biome 2.0. We will use this opportunity to remove deprecated features. We will make the migration smooth by using the <code dir="auto">biome migrate</code> command.</p>Biome v1.7https://biomejs.dev/blog/biome-v1-7/https://biomejs.dev/blog/biome-v1-7/This new version provides an easy path to migrate from ESLint and Prettier.
It also introduces machine-readable reports for the formatter and the linter, new linter rules, and many fixes.
Mon, 15 Apr 2024 00:00:00 GMT<p>Today we’re excited to announce the release of Biome v1.7!</p>
<p>This new version provides an easy path to migrate from ESLint and Prettier. It also introduces experimental machine-readable reports for the formatter and the linter, new linter rules, and many fixes.</p>
<p>Update Biome using the following commands:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>npm install --save-dev --save-exact @biomejs/biome@latest</span></div></div><div><div><span>npx @biomejs/biome migrate</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="migrate-from-eslint-with-a-single-command">Migrate from ESLint with a single command</h2></div>
<p>This release introduces a new subcommand
<code dir="auto">biome migrate eslint</code>. This command will read your ESLint configuration and attempt to port their settings to Biome.</p>
<p>The subcommand is able to handle both the legacy and the flat configuration files. It supports the
<code dir="auto">extends</code> field of the legacy configuration and loads both shared and plugin configurations!
The subcommand also migrates <code dir="auto">.eslintignore</code>.</p>
<p>Given the following ESLint configuration:</p>
<div><figure><figcaption><span>.eslintrc.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"extends"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>plugin:unicorn/recommended</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"plugins"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>unicorn</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"ignore\_patterns"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>dist/\*\*</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"globals"</span><span>: {</span></div></div><div><div><span> </span><span>"Global1"</span><span>: </span><span>"</span><span>readonly</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"eqeqeq"</span><span>: </span><span>"</span><span>error</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"overrides"</span><span>: [</span></div></div><div><div><span><span> </span></span><span>{</span></div></div><div><div><span> </span><span>"files"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>tests/\*\*</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"eqeqeq"</span><span>: </span><span>"</span><span>off</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>And the following Biome configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"recommended"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Run
<code dir="auto">biome migrate eslint --write</code> to migrate your ESLint configuration to Biome. The command overwrites your initial Biome configuration. For example, it disables
<code dir="auto">recommended</code>. This results in the following Biome configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"organizeImports"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"recommended"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"complexity"</span><span>: {</span></div></div><div><div><span> </span><span>"noForEach"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"noStaticOnlyClass"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"noUselessSwitchCase"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useFlatMap"</span><span>: </span><span>"</span><span>error</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"style"</span><span>: {</span></div></div><div><div><span> </span><span>"noNegationElse"</span><span>: </span><span>"</span><span>off</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useForOf"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useNodejsImportProtocol"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useNumberNamespace"</span><span>: </span><span>"</span><span>error</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"suspicious"</span><span>: {</span></div></div><div><div><span> </span><span>"noDoubleEquals"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"noThenProperty"</span><span>: </span><span>"</span><span>error</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"useIsArray"</span><span>: </span><span>"</span><span>error</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"globals"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>Global1</span><span>"</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"overrides"</span><span>: [</span></div></div><div><div><span><span> </span></span><span>{</span></div></div><div><div><span> </span><span>"include"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>tests/\*\*</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"suspicious"</span><span>: {</span></div></div><div><div><span> </span><span>"noDoubleEquals"</span><span>: </span><span>"</span><span>off</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The subcommand needs Node.js to load and resolve all the plugins and
<code dir="auto">extends</code> configured in the ESLint configuration file. For now,
<code dir="auto">biome migrate eslint</code> doesn’t support configuration written in YAML.</p>
<p>We have a <a href="https://biomejs.dev/linter/rules-sources/">dedicated page</a> that lists the equivalent Biome rule of a given ESLint rule. We handle some ESLint plugins such as <a href="https://typescript-eslint.io/">TypeScript ESLint</a>, <a href="https://github.com/jsx-eslint/eslint-plugin-jsx-a11y">ESLint JSX A11y</a>, <a href="https://github.com/jsx-eslint/eslint-plugin-react">ESLint React</a>, and <a href="https://github.com/sindresorhus/eslint-plugin-unicorn">ESLint Unicorn</a>. Some rules are equivalent to their ESLint counterparts, while others are inspired. By default, Biome doesn’t migrate inspired rules. You can use the CLI flag
<code dir="auto">--include-inspired</code> to migrate them.</p>
<div><h2 id="migrate-from-prettier-with-a-single-command">Migrate from Prettier with a single command</h2></div>
<p><a href="https://biomejs.dev/blog/biome-v1-6/#easier-migration-from-prettier">Biome v1.6 introduced the subcommand <code dir="auto">biome migrate prettier</code></a>.</p>
<p>In Biome v1.7, we add support of <a href="https://prettier.io/docs/en/configuration.html#configuration-overrides">Prettier’s
<code dir="auto">overrides</code></a> and attempts to convert
<code dir="auto">.prettierignore</code> glob patterns to globs supported by Biome.</p>
<p>During the migration, Prettier’s <code dir="auto">overrides</code> is translated to <a href="https://biomejs.dev/reference/configuration/#overrides">Biome’s
<code dir="auto">overrides</code></a>. Given the following <code dir="auto">.prettierrc.json</code></p>
<div><figure><figcaption><span>.prettierrc.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"useTabs"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"singleQuote"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"overrides"</span><span>: [</span></div></div><div><div><span><span> </span></span><span>{</span></div></div><div><div><span> </span><span>"files"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>\*.json</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"options"</span><span>: {</span></div></div><div><div><span> </span><span>"tabWidth"</span><span>: </span><span>2</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Run
<code dir="auto">biome migrate prettier --write</code> to migrate your Prettier configuration to Biome. This results in the following Biome configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"formatWithErrors"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"indentStyle"</span><span>: </span><span>"</span><span>space</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"indentWidth"</span><span>: </span><span>2</span><span>,</span></div></div><div><div><span> </span><span>"lineEnding"</span><span>: </span><span>"</span><span>lf</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lineWidth"</span><span>: </span><span>80</span><span>,</span></div></div><div><div><span> </span><span>"attributePosition"</span><span>: </span><span>"</span><span>auto</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"organizeImports"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"recommended"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"jsxQuoteStyle"</span><span>: </span><span>"</span><span>double</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"quoteProperties"</span><span>: </span><span>"</span><span>asNeeded</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"trailingComma"</span><span>: </span><span>"</span><span>all</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"semicolons"</span><span>: </span><span>"</span><span>asNeeded</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"arrowParentheses"</span><span>: </span><span>"</span><span>always</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"bracketSpacing"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"bracketSameLine"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"quoteStyle"</span><span>: </span><span>"</span><span>single</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"attributePosition"</span><span>: </span><span>"</span><span>auto</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"overrides"</span><span>: [</span></div></div><div><div><span><span> </span></span><span>{</span></div></div><div><div><span> </span><span>"include"</span><span>: [</span></div></div><div><div><span> </span><span>"</span><span>\*.json</span><span>"</span></div></div><div><div><span><span> </span></span><span>],</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"indentWidth"</span><span>: </span><span>2</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The subcommand needs Node.js to load JavaScript configurations such as <code dir="auto">.prettierrc.js</code>.
<code dir="auto">biome migrate prettier</code> doesn’t support configuration written in JSON5, TOML, or YAML.</p>
<div><h2 id="emit-machine-readable-reports">Emit machine-readable reports</h2></div>
<p>Biome is now able to output JSON reports detailing the diagnostics emitted by a command.</p>
<p>For instance, you can emit a report when you lint a codebase:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--reporter=json-pretty</span><span> </span><span>.</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>For now, we support two report formats: <code dir="auto">json</code> and <code dir="auto">json-pretty</code>.</p>
<p>Note that the report format is \*\*experimental
\*\*, and it might change in the future. Please try this feature and let us know if any information needs to be added to the reports.</p>
<div><h2 id="check-git-staged-files">Check <code dir="auto">git</code> staged files</h2></div>
<p>Biome v1.5 added the <code dir="auto">--changed</code> to format and lint <code dir="auto">git</code> tracked files that have been changed.</p>
<p>Today we are introducing a new option <code dir="auto">--staged</code> which allows you to check only files added to the <em>Git index</em> (<em>staged
files</em>). This is useful for checking that the files you want to commit are formatted and linted:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>check</span><span> </span><span>--staged</span><span> </span><span>.</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>This is handy for writing your own <a href="https://biomejs.dev/recipes/git-hooks/#shell-script">pre-commit script</a>. Note that unstaged changes on a staged file are
<strong>not</strong> ignored. Thus, we still recommend using a <a href="https://biomejs.dev/recipes/git-hooks/">dedicated pre-commit tool</a>.</p>
<p>Thanks to <a href="https://github.com/castarco">@castarco</a> for implementing this feature!</p>
<div><h2 id="linter">Linter</h2></div>
<div><h3 id="new-nursery-rules">New nursery rules</h3></div>
<p>Since <em>Biome
v1.6</em>, we added several new rules. New rules are incubated in the nursery group. Nursery rules are exempt from semantic versioning.</p>
<p>The new rules are:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-constant-math-min-max-clamp/">nursery/noConstantMathMinMaxClamp</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-done-callback/">nursery/noDoneCallback</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-else-if/">nursery/noDuplicateElseIf</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-evolving-types/">nursery/noEvolvingTypes</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-flat-map-identity/">nursery/noFlatMapIdentity</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misplaced-assertion/">nursery/noMisplacedAssertion</a></li>
</ul>
<div><h3 id="promoted-rules">Promoted rules</h3></div>
<p>Once stable, a nursery rule is promoted to a stable group. The following rules are promoted:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-excessive-nested-test-suites">complexity/noExcessiveNestedTestSuites</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-ternary/">complexity/noUselessTernary</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-jsx-key-in-iterable/">correctness/useJsxKeyInIterable</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-barrel-file/">performance/noBarrelFile</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-re-export-all/">performance/noReExportAll</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-namespace-import/">style/noNamespaceImport</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-node-assert-strict/">style/useNodeAssertStrict</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-test-hooks/">suspicious/noDuplicateTestHooks</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-exports-in-test/">suspicious/noExportsInTest</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-focused-tests/">suspicious/noFocusedTests</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-skipped-tests/">suspicious/noSkippedTests</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-suspicious-semicolon-in-jsx">suspicious/noSuspiciousSemicolonInJsx</a></li>
</ul>
<div><h2 id="miscellaneous">Miscellaneous</h2></div>
<ul>
<li>
<p>By default, Biome searches a configuration file in the working directory and parent directories if it doesn’t exist. Biome provides a CLI option
<code dir="auto">--config-path</code> and an environment variable
<code dir="auto">BIOME\_CONFIG\_PATH</code> that allows which can be used to override this behavior. Previously, they required a directory containing a Biome configuration file. For example, the following command uses the Biome configuration file in
<code dir="auto">./config/</code>.</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--config-path=./config/</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>This wasn’t very clear for many users who are used to specifying the configuration file path directly. They now accept a file, so the following command is valid:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--config-path=./config/biome.json</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>You can now ignore
<code dir="auto">React</code> imports in the rules <a href="https://biomejs.dev/linter/rules/no-unused-imports/#options">noUnusedImports</a> and <a href="https://biomejs.dev/linter/rules/use-import-type/#options">useImportType</a> by setting <a href="https://biomejs.dev/reference/configuration/#javascriptjsxruntime">
<code dir="auto">javascript.jsxRuntime</code></a> to <code dir="auto">reactClassic</code>.</p>
</li>
<li>
<p>Biome applies specific settings to <a href="https://biomejs.dev/guides/configure-biome/#well-known-files">well-known files</a>. It now recognizes more files and distinguishes between JSON files that only allow comments and JSON files that allow both comments and trailing commas.</p>
</li>
<li>
<p>In the React ecosystem, files ending in
<code dir="auto">.js</code> are allowed to contain JSX syntax. The Biome extension is now able to parse JSX syntax in files that are associated with the JavaScript language identifier.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-exhaustive-dependencies/">useExhaustiveDependencies</a> now supports Preact.</p>
</li>
</ul>
<p>See the <a href="https://biomejs.dev/internals/changelog/#170-2024-04-15">changelog</a> for more details.</p>
<div><h2 id="whats-next">What’s Next?</h2></div>
<p>We have started work on the CSS formatter and linter. Early implementation towards a <a href="https://github.com/biomejs/biome/discussions/2286">plugin system</a> is also underway. Some of our contributors have started preliminary work for <a href="https://github.com/biomejs/biome/issues/1927">
<em>GraphQL</em></a> and <a href="https://github.com/biomejs/biome/issues/2365">YAML</a>. Any help is welcome!</p>
<p>Follow us on <a href="https://bsky.app/profile/biomejs.dev">our BlueSky</a> and join <a href="https://biomejs.dev/chat">our Discord community</a>.</p>Biome v1.6https://biomejs.dev/blog/biome-v1-6/https://biomejs.dev/blog/biome-v1-6/Partial support for Astro, Svelte and Vue files, both CLI and LSP.
Now, the extends field is able to pick configuration files that are exported from a dependency.
The formatter has new options.
Fri, 08 Mar 2024 00:00:00 GMT<p>Update Biome using the following commands:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@latest</span></div></div><div><div><span>npx</span><span> </span><span>@biomejs/biome</span><span> </span><span>migrate</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="partial-support-for-astro-svelte-and-vue-files">Partial support for Astro, Svelte and Vue files</h2></div>
<p>In this release, we’re happy to provide partial support for Astro, Svelte and Vue files. What does <strong>partial</strong> support mean?</p>
<p>While the team is working on a <a href="https://github.com/biomejs/biome/discussions/1726">unified data structure</a> for HTML-ish languages, we discovered that we could provide Biome functionalities to those files with just a few changes, albeit with some limitations.</p>
<p>This means that Biome is able to analyze the JavaScript/TypeScript portion of said files, and all features are available: formatting, linting and import sorting! Here’s an example of what you should expect in terms of developer experience:</p>
<starlight-tabs> <div> <ul role="tablist"> <li role="presentation"> <a role="tab" href="#tab-panel-135" id="tab-135" aria-selected="true" tabindex="0"> <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M7.233 15.856c-.456 1.5-.132 3.586.948 4.57v-.036l.036-.096c.132-.636.648-1.032 1.309-1.008.612.012.96.336 1.044 1.044.036.264.036.528.048.803v.084c0 .6.168 1.176.504 1.68.3.48.72.851 1.284 1.103l-.024-.048-.024-.096c-.42-1.26-.12-2.135.984-2.879l.336-.227.745-.492a3.647 3.647 0 0 0 1.536-2.603c.06-.456 0-.9-.132-1.331l-.18.12c-1.668.887-3.577 1.2-5.425.84-1.117-.169-2.197-.48-3-1.416l.011-.012ZM2 15.592s3.205-1.559 6.421-1.559l2.437-7.508c.084-.36.348-.6.648-.6.3 0 .552.24.648.612l2.425 7.496c3.816 0 6.421 1.56 6.421 1.56L15.539.72c-.144-.444-.42-.72-.768-.72H8.24c-.348 0-.6.276-.768.72L2 15.592Z"></path></svg> Astro </a> </li><li role="presentation"> <a role="tab" href="#tab-panel-136" id="tab-136" aria-selected="false" tabindex="-1"> <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M6.117 1.659L12.000 11.870L17.883 1.659L14.775 1.659L12.000 6.469L9.225 1.659L6.117 1.659ZM23.951 1.659L19.178 1.659L12.000 14.090L4.822 1.659L0.049 1.659L12.000 22.341L23.951 1.659Z"></path></svg> Vue </a> </li><li role="presentation"> <a role="tab" href="#tab-panel-137" id="tab-137" aria-selected="false" tabindex="-1"> <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M10.924 1.248L5.422 4.734L10.924 1.248Q12.436 0.240 14.284 0.177Q16.132 0.114 17.812 0.933Q19.492 1.752 20.584 3.306L20.584 3.306Q21.382 4.398 21.676 5.721Q21.970 7.044 21.739 8.367Q21.508 9.690 20.794 10.740L20.794 10.740Q21.844 12.798 21.424 15.024L21.424 15.024Q21.214 16.242 20.542 17.292Q19.870 18.342 18.862 19.056L18.862 19.056L13.066 22.752Q11.554 23.760 9.706 23.823Q7.858 23.886 6.178 23.067Q4.498 22.248 3.406 20.694L3.406 20.694Q2.650 19.602 2.335 18.258Q2.020 16.914 2.272 15.612Q2.524 14.310 3.238 13.218L3.238 13.218Q2.146 11.202 2.566 8.976L2.566 8.976Q2.776 7.758 3.448 6.708Q4.120 5.658 5.128 4.944L5.128 4.944L10.924 1.248ZM18.316 4.776L18.316 4.776Q17.518 3.642 16.237 3.159Q14.956 2.676 13.612 3.012L13.612 3.012Q13.192 3.138 12.772 3.348L12.772 3.348L7.018 7.002Q6.304 7.422 5.863 8.094Q5.422 8.766 5.275 9.564Q5.128 10.362 5.317 11.160Q5.506 11.958 5.968 12.630L5.968 12.630Q6.766 13.764 8.047 14.226Q9.328 14.688 10.672 14.352L10.672 14.352Q11.092 14.226 11.512 14.016L11.512 14.016L13.864 12.546Q14.032 12.420 14.200 12.378L14.200 12.378Q14.620 12.294 15.019 12.420Q15.418 12.546 15.628 12.924L15.628 12.924Q15.922 13.302 15.838 13.806L15.838 13.806Q15.754 14.226 15.460 14.478L15.460 14.478L9.832 18.090Q9.664 18.216 9.496 18.258L9.496 18.258Q9.076 18.342 8.698 18.195Q8.320 18.048 8.089 17.733Q7.858 17.418 7.858 17.082L7.858 17.082L7.858 16.704L7.648 16.620Q6.682 16.326 5.842 15.780L5.842 15.780L5.212 15.360L5.128 15.654Q5.044 15.906 5.002 16.200L5.002 16.200Q4.834 16.998 5.023 17.796Q5.212 18.594 5.674 19.224L5.674 19.224Q6.430 20.316 7.627 20.799Q8.824 21.282 10.126 21.030L10.126 21.030L10.378 20.988Q10.840 20.862 11.218 20.652L11.218 20.652L17.014 16.998Q17.686 16.578 18.127 15.906Q18.568 15.234 18.715 14.436Q18.862 13.638 18.673 12.840Q18.484 12.042 18.022 11.370L18.022 11.370Q17.224 10.236 15.943 9.774Q14.662 9.312 13.318 9.648L13.318 9.648Q12.898 9.774 12.478 9.984L12.478 9.984L10.126 11.454Q9.958 11.580 9.790 11.622L9.790 11.622Q9.370 11.706 8.992 11.580Q8.614 11.454 8.362 11.076L8.362 11.076Q8.068 10.698 8.152 10.194L8.152 10.194Q8.236 9.774 8.530 9.522L8.530 9.522L14.158 5.910Q14.326 5.784 14.494 5.742L14.494 5.742Q14.914 5.658 15.292 5.805Q15.670 5.952 15.901 6.267Q16.132 6.582 16.132 6.918L16.132 6.918L16.132 7.296L16.342 7.380Q17.308 7.674 18.148 8.220L18.148 8.220L18.778 8.640L18.862 8.346Q18.946 8.052 18.988 7.800L18.988 7.800Q19.156 7.002 18.967 6.204Q18.778 5.406 18.316 4.776Z"></path></svg> Svelte </a> </li> </ul> </div> <div id="tab-panel-135" aria-labelledby="tab-135" role="tabpanel" tabindex="0"> <div align="center"><img src="https://biomejs.dev/\_astro/astro-linter.BfzFLjo-\_XOrzh.webp?dpl=69dce24b554af000071740e1" alt="Screenshot of Biome linting in action for an Astro file in VSCode" loading="lazy" decoding="async" fetchpriority="auto" width="500" height="593"></div> </div><div id="tab-panel-136" aria-labelledby="tab-136" role="tabpanel" tabindex="0" hidden> <div align="center"><img src="https://biomejs.dev/\_astro/vue-linter.BHM17JYs\_Zp1kLt.webp?dpl=69dce24b554af000071740e1" alt="Screenshot of Biome linting in action for an Vue file in VSCode" loading="lazy" decoding="async" fetchpriority="auto" width="500" height="593"></div> </div><div id="tab-panel-137" aria-labelledby="tab-137" role="tabpanel" tabindex="0" hidden> <div align="center"><img src="https://biomejs.dev/\_astro/svelte-linter.BLgKcKe\_\_Z2wDwJQ.webp?dpl=69dce24b554af000071740e1" alt="Screenshot of Biome linting in action for an Svelte file in VSCode" loading="lazy" decoding="async" fetchpriority="auto" width="500" height="593"></div> </div> </starlight-tabs>
<p>Make sure to read the <a href="https://biomejs.dev/internals/language-support#html-super-languages-support">documentation about expectations and limitations</a>.</p>
<div><h2 id="configuration-lighter-and-more-powerful">Configuration, lighter and more powerful</h2></div>
<div><h3 id="support-for-biomejsonc">Support for <code dir="auto">biome.jsonc</code></h3></div>
<p>Biome now accepts the <code dir="auto">biome.jsonc</code> file as configuration! You can insert all the comments you want in there.</p>
<div><h3 id="extends-resolves-dependencies"><code dir="auto">extends</code> resolves dependencies</h3></div>
<p>From this version, Biome can use the <code dir="auto">extends</code> property to <em>resolve</em> other configuration files that are inside installed dependencies.</p>
<p>There are few important steps in order to make the configuration discoverable. The file must be exported from a <code dir="auto">"module"</code> package, and the file should be exported in your <code dir="auto">package.json</code> like this:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"name"</span><span>: </span><span>"</span><span>@shared-configs</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"type"</span><span>: </span><span>"</span><span>module</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"exports"</span><span>: {</span></div></div><div><div><span> </span><span>"./biome"</span><span>: </span><span>"</span><span>./biome.json</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>This set up allows to expose a specifier <code dir="auto">@shared-configs/biome</code>, which you use inside your <code dir="auto">biome.json</code> file.</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"extends"</span><span>: [</span><span>"</span><span>@shared-configs/biome</span><span>"</span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The resolution of the dependencies is powered by the library <a href="https://github.com/oxc-project/oxc-resolver"><code dir="auto">oxc-resolver</code></a>, one of the many libraries provided by the <a href="https://oxc-project.github.io/">OXC project</a>. It’s battle-tested and spec compliant!</p>
<aside aria-label="Note"><p aria-hidden="true">Note</p><div><p>You can also export <code dir="auto">biome.jsonc</code> files!</p><div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"name"</span><span>: </span><span>"</span><span>@shared-configs</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"type"</span><span>: </span><span>"</span><span>module</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"exports"</span><span>: {</span></div></div><div><div><span> </span><span>"./biome"</span><span>: </span><span>"</span><ins><span>./biome.jsonc</span></ins><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div></div></aside>
<div><h3 id="reduced-memory-footprint">Reduced memory footprint</h3></div>
<p>We <strong>reduced</strong> the size our configuration <strong>by a factor of 6.5</strong>! This change might not have massive effects on the speed of the program, but it greatly reduced the memory used when running the CLI or the LSP.</p>
<div><h2 id="new-formatting-options">New formatting options</h2></div>
<p>Other than fixes, the formatter provides two new options that should improve the compatibility with Prettier.</p>
<div><h3 id="option-attributeposition">Option <code dir="auto">attributePosition</code></h3></div>
<p>When <code dir="auto">formatter.attributePosition</code> has the value <code dir="auto">multiline</code>, all attributes of HTML-ish languages (JSX/TSX as for time of writing) will be collapsed on multiple lines regardless of their numbers:</p>
<div><div><p></p><h4>With variant <code dir="auto">auto</code> (default)</h4>
The attributes are automatically formatted, and they will collapse in multiple lines only when they hit certain criteria.<p></p><div><figure><figcaption><span>file.jsx</span></figcaption><pre><code><div><div><span>&#x3C;</span><span>Button</span><span> </span><span>as</span><span>=</span><span>"</span><span>link</span><span>"</span><span> </span><span>style</span><span>=</span><span>"</span><span>primary</span><span>"</span><span> </span><span>href</span><span>=</span><span>"</span><span>https://example.com</span><span>"</span><span>></span></div></div><div><div><span><span> </span></span><span>Hit me</span></div></div><div><div><span>&#x3C;/</span><span>Button</span><span>></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div></div><div><p></p><h4>With variant <code dir="auto">multiline</code></h4>
The attributes are always formatted on multiple lines, regardless.<p></p><div><figure><figcaption><span>file.jsx</span></figcaption><pre><code><div><div><span>&#x3C;</span><span>Button</span></div></div><div><div><span> </span><span>as</span><span>=</span><span>"</span><span>link</span><span>"</span></div></div><div><div><span> </span><span>style</span><span>=</span><span>"</span><span>primary</span><span>"</span></div></div><div><div><span> </span><span>href</span><span>=</span><span>"</span><span>https://example.com</span><span>"</span></div></div><div><div><span>></span></div></div><div><div><span><span> </span></span><span>Hit me</span></div></div><div><div><span>&#x3C;/</span><span>Button</span><span>></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div></div></div>
<p>The contributor <a href="https://github.com/octoshikari">@octoshikari</a> implemented this new feature by themselves! Huge thank you for helping the Biome project.</p>
<div><h3 id="option-jsonformattertrailingcommas">Option <code dir="auto">json.formatter.trailingCommas</code></h3></div>
<p>Previously, Biome parser introduced an option that would allow to parse JSON and JSONC files that contained a trailing comma. This was required to ease the friction caused by other tools that
tolerate trailing commas by default (e.g. VSCode, Prettier, etc.).</p>
<p>Unfortunately, our formatter wasn’t as tolerant. But with this release, we’ve introduced the option <code dir="auto">json.formatter.trailingCommas</code>. It allows you to apply the same rules as with <code dir="auto">js.formatter.trailingComma</code>.</p>
<div><div><p></p><h4>With variant <code dir="auto">none</code> (default)</h4>
The formatter removes the trailing comma upon formatting.<p></p><div><figure><figcaption><span>file.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><ins><span>"</span><span>ipsum\_last</span><span>"</span></ins></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div></div><div><p></p><h4>With variant <code dir="auto">all</code></h4>
The formatter adds the trailing comma upon formatting.<p></p><div><figure><figcaption><span>file.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><span>"</span><span>ipsum</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lorem"</span><span>: </span><ins><span>"</span><span>ipsum\_last</span><span>"</span><span>,</span></ins></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div></div></div>
<div><h2 id="easier-migration-from-prettier">Easier migration from Prettier</h2></div>
<p>This release introduces a new command called <code dir="auto">biome migrate prettier</code>. This command will read your Prettier <code dir="auto">.prettierrc</code>/<code dir="auto">prettier.json</code> and <code dir="auto">.prettierignore</code>, and attempt to port its options and globs in Biome.</p>
<p>Given a <code dir="auto">prettier.json</code> file, Biome will <strong>modify</strong> the existing configuration file to match Prettier’s options:</p>
<div><figure><figcaption><span>prettier.json</span></figcaption><pre><code><div><div><span>{ </span><span>"useTabs"</span><span>: </span><span>false</span><span>, </span><span>"semi"</span><span>: </span><span>true</span><span>, </span><span>"singleQuote"</span><span>: </span><span>true</span><span> }</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"formatWithErrors"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"indentStyle"</span><span>: </span><span>"</span><span>space</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"indentWidth"</span><span>: </span><span>2</span><span>,</span></div></div><div><div><span> </span><span>"lineEnding"</span><span>: </span><span>"</span><span>lf</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"lineWidth"</span><span>: </span><span>80</span><span>,</span></div></div><div><div><span> </span><span>"attributePosition"</span><span>: </span><span>"</span><span>auto</span><span>"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span> </span><span>"linter"</span><span>: { </span><span>"enabled"</span><span>: </span><span>true</span><span> },</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"jsxQuoteStyle"</span><span>: </span><span>"</span><span>double</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"quoteProperties"</span><span>: </span><span>"</span><span>asNeeded</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"trailingCommas"</span><span>: </span><span>"</span><span>all</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"semicolons"</span><span>: </span><span>"</span><span>always</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"arrowParentheses"</span><span>: </span><span>"</span><span>always</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"bracketSpacing"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"bracketSameLine"</span><span>: </span><span>false</span><span>,</span></div></div><div><div><span> </span><span>"quoteStyle"</span><span>: </span><span>"</span><span>single</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"attributePosition"</span><span>: </span><span>"</span><span>auto</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<aside aria-label="Caution"><p aria-hidden="true">Caution</p><div><p>Due to the different nature of <code dir="auto">.prettierignore</code> globs and Biome’s globs, it’s <strong>highly advised</strong> to make sure that those globs still work under Biome.
Prettier’s globs are <strong>git globs</strong>, while Biome’s globs are <strong>unix-style</strong> globs.</p></div></aside>
<div><h3 id="linter">Linter</h3></div>
<div><h4 id="promoted-rules">Promoted rules</h4></div>
<p>New rules are incubated in the nursery group.
Once stable, we promote them to a stable group.
The following rules are promoted:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-empty-type-parameters">complexity/noEmptyTypeParameters</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-lone-block-statements">complexity/noUselessLoneBlockStatements</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unused-imports">correctness/noUnusedImports</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-use-before-declaration">correctness/noInvalidUseBeforeDeclaration</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-unused-private-class-members">correctness/noUnusedPrivateClassMembers</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-await">suspicious/useAwait</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-global-eval">security/noGlobalEval</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-consistent-array-type">style/useConsistentArrayType</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-export-type">style/useExportType</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-filenaming-convention">style/useFilenamingConvention</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-for-of">style/useForOf</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-import-type">style/useImportType</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-nodejs-import-protocol">style/useNodejsImportProtocol</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-number-namespace">style/useNumberNamespace</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-shorthand-function-type">style/useShorthandFunctionType</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-empty-block-statements">suspicious/noEmptyBlockStatements</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-global-assign">suspicious/noGlobalAssign</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misleading-character-class">suspicious/noMisleadingCharacterClass</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-then-property">suspicious/noThenProperty</a></li>
</ul>
<p>Additionally, the following rules are now recommended:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-approximative-numeric-constant">suspicious/noApproximativeNumericConstant</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misrefactored-shorthand-assign">suspicious/noMisrefactoredShorthandAssign</a></li>
</ul>
<div><h4 id="removed-rules">Removed rules</h4></div>
<ul>
<li>Remove <code dir="auto">nursery/useGroupedTypeImport</code>. The rule <a href="https://biomejs.dev/linter/rules/use-import-type">style/useImportType</a> covers the behavior of this rule.</li>
</ul>
<div><h4 id="new-rules">New rules</h4></div>
<p>New rules are now available:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-barrel-file">nursery/noBarrelFile</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-exports-in-test">nursery/noExportsInTest</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-focused-tests">nursery/noFocusedTests</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-namespace-import">nursery/noNamespaceImport</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-semicolon-in-jsx">nursery/noSemicolonInJsx</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-skipped-tests">nursery/noSkippedTests</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-undeclared-dependencies">nursery/noUndeclaredDependencies</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-node-assert-strict">nursery/useNodeAssertStrict</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-sorted-classes">nursery/useSortedClasses</a></li>
</ul>
<div><h3 id="miscellaneous">Miscellaneous</h3></div>
<ul>
<li>We drastically reduced the number of protected files, which means you can now format your <code dir="auto">package.json</code>, <code dir="auto">tsconfig.json</code>, etc. with Biome. Lock files are still considered protected.</li>
<li>The CLI now does a better job at reporting the total number of files and the files that were really changed.</li>
<li>When a diagnostic shows a file name on the terminal that is integrated with your editor, you can click it and the editor will open the file for you.</li>
<li>The command <code dir="auto">biome rage</code> now accepts two nice options: <code dir="auto">--formatter</code> and <code dir="auto">--linter</code>.</li>
<li>We removed some superfluous error diagnostic when running the <code dir="auto">biome check</code> command.</li>
</ul>Biome v1.5https://biomejs.dev/blog/biome-v1-5/https://biomejs.dev/blog/biome-v1-5/This version has few features around the CLI and many fixes in our formatter.
The TypeScript, JSX and JavaScript formatter has surpassed the 97% compatibility rate with Prettier.
Biome now provides over 190 lint rules.
Mon, 08 Jan 2024 00:00:00 GMT<p>Along with the <a href="https://biomejs.dev/blog/roadmap-2024">Roadmap for 2024</a>, the <a href="https://biomejs.dev/blog/roadmap-2024#new-logo-and-homepage">new logo and homepage</a>, we also published a new version. This version has few features around the CLI and
<strong>many</strong> fixes in our formatter. Our TypeScript, JSX and JavaScript formatting has surpassed the <strong>97% compatibility
rate</strong> with Prettier. Biome now provides <strong>over 190 lint rules</strong>.</p>
<p>Update Biome using the following commands:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@latest</span></div></div><div><div><span>npx</span><span> </span><span>@biomejs/biome</span><span> </span><span>migrate</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="new-features">New features</h2></div>
<ul>
<li>Process only the files that were changed.</li>
<li>The command <code dir="auto">biome ci</code> now prints diagnostics in GitHub PRs.</li>
<li>A new command,<code dir="auto">biome explain</code>.</li>
<li>The command <code dir="auto">biome migrate</code> updates the <code dir="auto">$schema</code>.</li>
<li>New lint rules.</li>
</ul>
<div><h3 id="process-only-the-files-that-were-changed">Process only the files that were changed</h3></div>
<p>If you enable the integration with VCS, you can tell Biome to process only the files that were changed. As for now, this feature computes the files that were changed by using a VCS, so Biome doesn’t know exactly which lines changed.</p>
<p>This feature practically makes some utilities such as <code dir="auto">lint-staged</code> obsolete.</p>
<p>To take advantage of this feature, you have to tell Biome what’s the default branch in the configuration file, and then you’ll have to pass the option <code dir="auto">--changed</code> via CLI:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"vcs"</span><span>: {</span></div></div><div><div><span> </span><span>"enabled"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"clientKind"</span><span>: </span><span>"</span><span>git</span><span>"</span><span>,</span></div></div><div><div><span> </span><span>"defaultBranch"</span><span>: </span><span>"</span><span>main</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Once you modified some files, use the new option to the command you need, for example the <code dir="auto">format</code> command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><ins><span>--changed</span></ins><span> </span><span>--write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="the-command-biome-ci-now-prints-diagnostics-in-github-prs">The command <code dir="auto">biome ci</code> now prints diagnostics in GitHub PRs</h3></div>
<p>For quite some time, users were confused by the difference between the commands <code dir="auto">check</code> and <code dir="auto">ci</code>because, until now, their behaviours have been very similar. From this version, the command <code dir="auto">ci</code> can detect the GitHub CI environment and print annotation in the PRs.</p>
<p><img alt="Screenshot of a GitHub annotation printed by Biome" loading="lazy" decoding="async" fetchpriority="auto" width="610" height="170" src="https://biomejs.dev/\_astro/github-annotation.B\_unxUGt\_1ggJY8.webp?dpl=69dce24b554af000071740e1"></p>
<p>It’s possible that you would need to change your permissions of your workflow files in case you don’t see the annotations:</p>
<div><figure><figcaption><span>.github/workflows/action.yml</span></figcaption><pre><code><div><div><span>permissions</span><span>:</span></div></div><div><div><span> </span><span>pull-requests</span><span>: </span><span>write</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="a-new-command-biome-explain">A new command <code dir="auto">biome explain</code></h3></div>
<p>This command will serve as an “offline” documentation tool. In this release, the command supports the explanation of all the lint rules; for example you can request documentation for <code dir="auto">noAccumulatingSpread</code>:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>explain</span><span> </span><span>noAccumulatingSpread</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Which will print the following Markdown:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span># noAccumulatingSpread</span></div></div><div><div>
</div></div><div><div><span>No fix available.</span></div></div><div><div>
</div></div><div><div><span>This rule is recommended.</span></div></div><div><div>
</div></div><div><div><span># Description</span></div></div><div><div>
</div></div><div><div><span>Disallow the use of spread (</span><span>`...`</span><span>) syntax on accumulators.</span></div></div><div><div>
</div></div><div><div><span>Spread syntax allows an iterable to be expanded into its individual elements.</span></div></div><div><div>
</div></div><div><div><span>Spread syntax should be avoided on accumulators (like those in </span><span>`.reduce`</span><span>)</span></div></div><div><div><span>because it causes a time complexity of </span><span>`O(n^2)`</span><span> instead of </span><span>`O(n)`</span><span>.</span></div></div><div><div>
</div></div><div><div><span>Source: https://prateeksurana.me/blog/why-using-object-spread-with-reduce-bad-idea/</span></div></div><div><div>
</div></div><div><div><span>## Examples</span></div></div><div><div>
</div></div><div><div><span>### Invalid</span></div></div><div><div>
</div></div><div><div><span>```js,expect\_diagnostic</span></div></div><div><div><span>var </span><span>a</span><span> =</span><span> [</span><span>'</span><span>a</span><span>'</span><span>, </span><span>'</span><span>b</span><span>'</span><span>, </span><span>'</span><span>c</span><span>'</span><span>];</span></div></div><div><div><span>a</span><span>.</span><span>reduce</span><span>(</span><span>(</span><span><span>acc</span><span>, </span><span>val</span></span><span>)</span><span> </span><span>=></span><span> [</span><span>...</span><span><span>acc</span><span>, </span><span>val</span><span>], []);</span></span></div></div><div><div><span>```</span></div></div><div><div>
</div></div><div><div><span>```js,expect\_diagnostic</span></div></div><div><div><span>var </span><span>a</span><span> =</span><span> [</span><span>'</span><span>a</span><span>'</span><span>, </span><span>'</span><span>b</span><span>'</span><span>, </span><span>'</span><span>c</span><span>'</span><span>];</span></div></div><div><div><span>a</span><span>.</span><span>reduce</span><span>(</span><span>(</span><span><span>acc</span><span>, </span><span>val</span></span><span>)</span><span> </span><span>=></span><span> {</span><span>return</span><span> [</span><span>...</span><span><span>acc</span><span>, </span><span>val</span><span>];}, []);</span></span></div></div><div><div><span>```</span></div></div><div><div>
</div></div><div><div><span>```js,expect\_diagnostic</span></div></div><div><div><span>var </span><span>a</span><span> =</span><span> [</span><span>'</span><span>a</span><span>'</span><span>, </span><span>'</span><span>b</span><span>'</span><span>, </span><span>'</span><span>c</span><span>'</span><span>];</span></div></div><div><div><span>a</span><span>.</span><span>reduce</span><span>(</span><span>(</span><span><span>acc</span><span>, </span><span>val</span></span><span>)</span><span> </span><span>=></span><span> ({</span><span>...</span><span><span>acc</span><span>, [</span><span>val</span><span>]: </span><span>val</span><span>}), {});</span></span></div></div><div><div><span>```</span></div></div><div><div>
</div></div><div><div><span>## Valid</span></div></div><div><div>
</div></div><div><div><span>```js</span></div></div><div><div><span>var </span><span>a</span><span> =</span><span> [</span><span>'</span><span>a</span><span>'</span><span>, </span><span>'</span><span>b</span><span>'</span><span>, </span><span>'</span><span>c</span><span>'</span><span>];</span></div></div><div><div><span>a</span><span>.</span><span>reduce</span><span>(</span><span>(</span><span><span>acc</span><span>, </span><span>val</span></span><span>)</span><span> </span><span>=></span><span> {</span><span>acc</span><span>.</span><span>push</span><span><span>(</span><span>val</span><span>); </span></span><span>return</span><span><span> </span><span>acc</span><span>}, []);</span></span></div></div><div><div><span>```</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>We plan to make this output more readable for terminals, as well as provide autocompletion for this command.</p>
<div><h4 id="the-command-biome-migrate-updates-the-schema">The command <code dir="auto">biome migrate</code> updates the <code dir="auto">$schema</code></h4></div>
<p>The command <code dir="auto">biome migrate</code> now updates the <code dir="auto">$schema</code> value inside the configuration file <code dir="auto">biome.json</code> if you avail of the online schema. Run this command as soon as you update to Biome <code dir="auto">v1.5.0</code>:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"$schema"</span><span>: </span><span>"</span><span>https://biomejs.dev/schemas/1.4.1/schema.json</span><span>"</span></div></div><div><div><span> </span><span>"</span><span>$schema</span><span>"</span><span>:</span><span> </span><span>"</span><span>https://biomejs.dev/schemas/</span><ins><span>1.5.0</span></ins><span>/schema.json</span><span>"</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="new-rules">New rules</h3></div>
<div><h4 id="useexporttype"><a href="https://biomejs.dev/linter/rules/use-export-type">useExportType</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>interface</span><span> I {</span></div></div><div><div><span>}</span></div></div><div><div>
</div></div><div><div><span>export</span><span> {I};</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useExportType.js:2:8 <a href="https://biomejs.dev/linter/rules/use-export-type">lint/nursery/useExportType</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>All exports are only types and should thus use </span><span><strong>export type</strong></span><span>.</span>
<strong>1 │ </strong>interface I {}
<strong><span> </span></strong><strong><span>></span></strong> <strong>2 │ </strong>export { I };
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>3 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Using </span><span><strong>export type</strong></span><span> allows transpilers to safely drop exports of types without looking for their definition.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Safe fix</span><span>: </span><span>Use a grouped </span><span><strong>export type</strong></span><span>.</span>
<strong> </strong><strong> 2 │ </strong>export<span>·</span><span>t</span><span>y</span><span>p</span><span>e</span><span><span>·</span></span>{<span>·</span>I<span>·</span>};
<strong> </strong><strong> │ </strong> <span>+</span><span>+</span><span>+</span><span>+</span><span>+</span>
</code></pre>
<div><h4 id="useimporttype"><a href="https://biomejs.dev/linter/rules/use-import-type">useImportType</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>import</span><span> {A} </span><span>from</span><span> </span><span>"</span><span>./mod.js</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>type</span><span> TypeOfA </span><span>=</span><span> </span><span>typeof</span><span> </span><span>A</span><span>;</span></div></div><div><div><span>let </span><span>a</span><span>:</span><span> </span><span>A</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useImportType.js:1:1 <a href="https://biomejs.dev/linter/rules/use-import-type">lint/nursery/useImportType</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>All these imports are only used as types.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>import { A } from "./mod.js";
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>type TypeOfA = typeof A;
<strong>3 │ </strong>let a: A;
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Importing the types with </span><span><strong>import type</strong></span><span> ensures that they are removed by the transpilers and avoids loading unnecessary modules.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Safe fix</span><span>: </span><span>Use </span><span><strong>import type</strong></span><span>.</span>
<strong> </strong><strong> 1 │ </strong>import<span>·</span><span>t</span><span>y</span><span>p</span><span>e</span><span><span>·</span></span>{<span>·</span>A<span>·</span>}<span>·</span>from<span>·</span>"./mod.js";
<strong> </strong><strong> │ </strong> <span>+</span><span>+</span><span>+</span><span>+</span><span>+</span>
</code></pre>
<div><h4 id="usefilenamingconvention"><a href="https://biomejs.dev/linter/rules/use-filenaming-convention">useFilenamingConvention</a></h4></div>
<p>Enforces naming conventions for JavaScript and TypeScript filenames.</p>
<div><h4 id="usenodejsimportprotocol"><a href="https://biomejs.dev/linter/rules/use-nodejs-import-protocol">useNodejsImportProtocol</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>import</span><span> fs </span><span>from</span><span> </span><span>'</span><span>fs</span><span>'</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useNodejsImportProtocol.js:1:16 <a href="https://biomejs.dev/linter/rules/use-nodejs-import-protocol">lint/nursery/useNodejsImportProtocol</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>⚠</span></strong> <span>Import from Node.js builtin module "</span><span><strong>fs</strong></span><span>" should use the "</span><span><strong>node:</strong></span><span>" protocol.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>import fs from 'fs';
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Using the </span><span><strong>node:</strong></span><span> protocol is more explicit and signals that the imported module belongs to Node.js.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Unsafe fix</span><span>: </span><span>Change to "node:fs".</span>
<strong>1</strong> <strong> │ </strong><span>-</span> <span>i</span><span>m</span><span>p</span><span>o</span><span>r</span><span>t</span><span><span>·</span></span><span>f</span><span>s</span><span><span>·</span></span><span>f</span><span>r</span><span>o</span><span>m</span><span><span>·</span></span><span><strong>'</strong></span><span><strong>f</strong></span><span><strong>s</strong></span><span><strong>'</strong></span><span>;</span>
<strong>1</strong><strong> │ </strong><span>+</span> <span>i</span><span>m</span><span>p</span><span>o</span><span>r</span><span>t</span><span><span>·</span></span><span>f</span><span>s</span><span><span>·</span></span><span>f</span><span>r</span><span>o</span><span>m</span><span><span>·</span></span><span><strong>"</strong></span><span><strong>n</strong></span><span><strong>o</strong></span><span><strong>d</strong></span><span><strong>e</strong></span><span><strong>:</strong></span><span><strong>f</strong></span><span><strong>s</strong></span><span><strong>"</strong></span><span>;</span>
<strong>2</strong> <strong>2</strong><strong> │ </strong>
</code></pre>
<div><h4 id="nonodejsmodules"><a href="https://biomejs.dev/linter/rules/no-nodejs-modules">noNodejsModules</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>import</span><span> fs </span><span>from</span><span> </span><span>"</span><span>fs</span><span>"</span><span>;</span></div></div><div><div><span>import</span><span> path </span><span>from</span><span> </span><span>"</span><span>node:path</span><span>"</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noNodejsModules.js:1:16 <a href="https://biomejs.dev/linter/rules/no-nodejs-modules">lint/nursery/noNodejsModules</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>⚠</span></strong> <span>Using Node.js modules are forbidden.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>import fs from "fs";
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>import path from "node:path";
<strong>3 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Can be useful for client-side web projects that do not have access to those modules.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Remove the import module.</span>
</code></pre>
<div><h4 id="noinvalidusebeforedeclaration"><a href="https://biomejs.dev/linter/rules/no-invalid-use-before-declaration">noInvalidUseBeforeDeclaration</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>function</span><span> </span><span>f</span><span>()</span><span> {</span></div></div><div><div><span> </span><span>console</span><span>.</span><span>log</span><span><span>(</span><span>x</span><span>);</span></span></div></div><div><div><span> </span><span>const </span><span>x</span><span>;</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noInvalidUseBeforeDeclaration.js:3:11 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Const declarations must have an initialized value.</span>
<strong>1 │ </strong>function f() {
<strong>2 │ </strong> console.log(x);
<strong><span> </span></strong><strong><span>></span></strong> <strong>3 │ </strong> const x;
<strong> │ </strong> <strong><span>^</span></strong>
<strong>4 │ </strong>}
<strong>5 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>This variable needs to be initialized.</span>
</code></pre>
<div><h4 id="noglobaleval"><a href="https://biomejs.dev/linter/rules/no-global-eval">noGlobalEval</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>eval</span><span>(</span><span>"</span><span>var a = 0</span><span>"</span><span>);</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noGlobalEval.js:1:1 <a href="https://biomejs.dev/linter/rules/no-global-eval">lint/nursery/noGlobalEval</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span><strong>eval()</strong></span><span> exposes to security risks and performance issues.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>eval("var a = 0");
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>See the </span><span><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/eval#never\_use\_eval!">MDN web docs</a></span><span> for more details.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Refactor the code so that it doesn't need to call </span><span><strong>eval()</strong></span><span>.</span>
</code></pre>
<div><h4 id="noglobalassign"><a href="https://biomejs.dev/linter/rules/no-global-assign">noGlobalAssign</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span><span>Object</span><span> </span></span><span>=</span><span> </span><span>null</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noGlobalAssign.js:1:1 <a href="https://biomejs.dev/linter/rules/no-global-assign">lint/nursery/noGlobalAssign</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>A global variable should not be reassigned.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>Object = null;
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Assigning to a global variable can override essential functionality.</span>
</code></pre>
<div><h4 id="nomisleadingcharacterclass"><a href="https://biomejs.dev/linter/rules/no-misleading-character-class">noMisleadingCharacterClass</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>/</span><span>^</span><span>[Á]</span><span>$</span><span>/</span><span>u</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noMisleadingCharacterClass.js:1:1 <a href="https://biomejs.dev/linter/rules/no-misleading-character-class">lint/nursery/noMisleadingCharacterClass</a> ━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>⚠</span></strong> <span>Unexpected combined character in the character class.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>/^[Á]$/u;
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
</code></pre>
<div><h4 id="nothenproperty"><a href="https://biomejs.dev/linter/rules/no-then-property">noThenProperty</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>const </span><span>foo</span><span> = {</span></div></div><div><div><span> </span><span>then</span><span>()</span><span> {</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noThenProperty.js:2:5 <a href="https://biomejs.dev/linter/rules/no-then-property">lint/nursery/noThenProperty</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Do not add </span><span><strong>then</strong></span><span> to an object.</span>
<strong>1 │ </strong>const foo = {
<strong><span> </span></strong><strong><span>></span></strong> <strong>2 │ </strong> then() {}
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>3 │ </strong>};
<strong>4 │ </strong>
</code></pre>
<div><figure><figcaption></figcaption><pre><code><div><div><span>const </span><span>foo</span><span> = {</span></div></div><div><div><span><span> </span></span><span>get </span><span>then</span><span>()</span><span> {</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h4 id="nouselessternary"><a href="https://biomejs.dev/linter/rules/no-useless-ternary">noUselessTernary</a></h4></div>
<div><figure><figcaption></figcaption><pre><code><div><div><span>var </span><span>a</span><span> = </span><span>x</span><span> ? </span><span>true</span><span> : </span><span>true</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noUselessTernary.js:1:9 <a href="https://biomejs.dev/linter/rules/no-useless-ternary">lint/nursery/noUselessTernary</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Unnecessary use of boolean literals in conditional expression.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>var a = x ? true : true;
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Simplify your code by directly assigning the result without using a ternary operator.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>If your goal is negation, you may use the logical NOT (!) or double NOT (!!) operator for clearer and concise code.
</span><span> </span><span> </span><span> Check for more details about </span><span><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical\_NOT">NOT</a></span><span> operator.</span>
</code></pre>Roadmap 2024https://biomejs.dev/blog/roadmap-2024/https://biomejs.dev/blog/roadmap-2024/Roadmap 2024, new logo and homepage
Mon, 08 Jan 2024 00:00:00 GMT<p>We are thrilled to share what the Core Contributors and Maintainers would like to focus on in 2024.</p>
<p>We want to remind you that Biome is a community-driven project, so we can only promise that some of the ideas outlined below will be shipped.</p>
<p>However, if you’re excited about some aspects of the project, and you want to see some of them developed faster than others, you can help us in many ways:</p>
<ul>
<li><a href="https://github.com/biomejs"><strong>Be involved in the project and the community</strong></a>. Please help us to build those features.</li>
<em>advertisement</em> for your company.</li>
<li><a href="https://biomejs.dev/guides/getting-started"><strong>Improve our documentation with ideas, recipes, or guides</strong></a>. Translate our documentation and help us to make Biome available to people who aren’t proficient in English.</li>
</ul>
<div><h2 id="preface">Preface</h2></div>
<p>The project is young and can’t compete against giants such as Prettier, ESLint, Webpack, Vite, ESBuild, etc. However, the recent events (sponsors, bounty challenge, Biome being a fork of Rome) showed that the users
<strong>have</strong> interest in the project, and we showed those users that we have the tools to fulfil a need.</p>
<p>Moving small projects from ESLint/Prettier is easy, but moving <strong>big</strong> code bases is challenging and time-consuming; this is a big friction point in Biome.</p>
<p>Users have different needs, though, so it will only be possible to satisfy some of them. We want to ensure that all features and contributions to our project <a href="https://biomejs.dev/internals/philosophy/">embrace our philosophy</a> and provide the best experience by default.</p>
<div><h2 id="main-area-of-focus">Main area of focus</h2></div>
<ol>
<li>Help users to move to Biome</li>
<li>Expand Biome’s language support so Biome tools can span more of the web ecosystem</li>
<li>Deepen Biome’s existing capabilities to offer more functionalities</li>
<li>Plugins</li>
<li>Transformations</li>
<li>Community and content</li>
</ol>
<div><h2 id="help-users-to-move-to-biome">Help users to move to Biome</h2></div>
<ul>
<li>Offer guides on our website to users who want to migrate from Prettier (CLI commands and configuration)</li>
<li>Offer guides on our website to users who want to migrate from ESlint (CLI commands and configuration)</li>
<li>Offer a section on our website that shows a mapping of the ESLint rules to our rules</li>
<li>Offer commands to ease the transition
<ul>
<li>A command called <code dir="auto">biome migrate prettier</code> that will read <code dir="auto">.prettierrc</code> and <code dir="auto">.prettierignore</code> will update the <code dir="auto">biome.json</code> file (or create it) with the configuration from the Prettier files.</li>
<li>A command called <code dir="auto">biome migrate eslint</code> will read the JSON configuration of Eslint and the ignore file. There will be expectations and limitations.</li>
</ul>
</li>
</ul>
<div><h2 id="expand-biomes-language-support">Expand Biome’s language support</h2></div>
<p>CSS is our next language of focus, and we are making good progress. HTML and Markdown will follow. Follow our <a href="https://biomejs.dev/internals/language-support">up-to-date page</a> to keep up with the progress of our work.</p>
<p>The CSS language will enable much work and experimentation: CSS formatting and linting, and we will port some of the lint rules from <code dir="auto">stylelint</code>. A new area of experimentation is cross-linting.</p>
<p>The idea of cross-linting can be explained with an example: compute the CSS styles/classes defined in a project and warn a user when said styles aren’t used inside JSX/HTML files.</p>
<p>Plus, we unlock another area of experimentation, which is embedded formatting.</p>
<p>HTML and Markdown will be our next languages of focus. HTML will enable us to parse other variants of HTML that are popular in the frontend ecosystem: <a href="https://vuejs.org/">Vue</a>, <a href="https://svelte.dev/">Svelte</a> and <a href="https://astro.build/">Astro</a>, and this would require some exploration of how to represent super languages of HTML.</p>
<div><h2 id="deepen-biomes-existing-capabilities-to-offer-more-functionalities">Deepen Biome’s existing capabilities to offer more functionalities.</h2></div>
<ul>
<li>Project analysis and dependency resolution</li>
<li>Type system</li>
<li>CLI</li>
</ul>
<div><h3 id="project-analysis-and-dependency-resolution">Project analysis and dependency resolution</h3></div>
<p>We will provide lint rules to read the manifest and detect errors such as invalid licenses.</p>
<p>With project resolution, we will be able to provide more lint rules, some of which will be able to detect unused modules.</p>
<p>With dependency resolution, we can - for example - detect dependencies that aren’t used inside a project.</p>
<p>With this infrastructure, our LSP is going to be more powerful and provide more features, for example:</p>
<ul>
<li>rename variables across a project;</li>
<li>auto-complete for imports;</li>
<li>in-line types</li>
</ul>
<div><h3 id="type-system">Type system</h3></div>
<p>Building a full-fledged type system such as TypeScript is a massive effort; that’s why we decided to take a different direction and start by building a subset of the type system that requires stricter typing. This approach would allow us to build some important lint rules that users have been asking for.</p>
<p>This will come with a downside: we will have to rely on a stricter code and minimal type inference from the compiler.</p>
<p>Once we have something we can rely on, we can slowly widen the capabilities of our type system.</p>
<div><h3 id="cli">CLI</h3></div>
<p>More features for the command line tool, such as:</p>
<ul>
<li>Add the <code dir="auto">explain</code> command for offline documentation;</li>
<li>Allow the output to be exported in different formats (JSON, etc.)</li>
<li>Auto-completion for other shells such as <code dir="auto">zsh</code>;</li>
<li>Implement the <code dir="auto">--modified</code> argument, which allows to format - for example - only the modified lines of a document;</li>
<li>Expose metrics for Biome’s operations and being able to track down possible performance bottlenecks;</li>
</ul>
<div><h2 id="plugins">Plugins</h2></div>
<p>We will explore plugins and come up with a design that fits Biome. Biome is different from other tools because Biome is a toolchain that has multiple tools in it, so we have to think out of the box and propose a design that might differ from the tools people are used to.</p>
<p>We don’t know yet what a Biome’s plugin will look like, although a plugin should be able to tap all the tools that Biome offers.</p>
<p>Some ideas that we will consider:</p>
<ul>
<li>DSL</li>
<li>WASM</li>
<li>A Runtime</li>
</ul>
<div><h2 id="transformations">Transformations</h2></div>
<p>Transformations and code generation will be our first steps towards our compiler.</p>
<p>We will provide the ability to transform TypeScript and JSX files into JavaScript files.</p>
<div><h2 id="community-and-content">Community and content</h2></div>
<p>Biome has a growing ecosystem, with an official VSCode extension, an official IntelliJ extension, and a Discord bot. We want to grow the features these tools provide and welcome anyone who wants to help us.</p>
<p>Our community is slowly growing, and we want to reward everyone who sticks around and contributes to Biome. At Biome, <strong>we value every contribution</strong>, so you don’t need to be proficient in Rust to help us. Even participating in discussions and helping us to shape our features or helping other people are considered
<em>contributions</em>. If you’d like to continue contributing to our ecosystem, we also encourage you to <a href="https://github.com/biomejs/biome/blob/main/GOVERNANCE.md#maintainer-nomination">nominate yourself as a maintainer of the project</a>.</p>
<p>Recently Biome started its own <a href="https://www.youtube.com/channel/UC6ssscaFgCSlbv1Pb6krGVw">YouTube Channel</a>. We will use this channel to share learning content with the community.</p>
<div><h2 id="new-logo-and-homepage">New logo and homepage</h2></div>
<p>With this blog post, we also want to officially announce our new logo, homepage and rebranding of the website.</p>
<p>With this new logo, we want to give a different meaning to the project. Biome <strong>isn’t</strong> a fork of Rome anymore, but a self-sufficient project ready to bloom.</p>
<p>The triangle of the logo represents the mountains - <strong>soil</strong> -, and the curly shape on the bottom left represents a wave of the ocean - <strong>water</strong>. Two elements that are important in creating a self-sufficient ecosystem, so it can thrive and grow.</p>Biome formatter wins the Prettier challengehttps://biomejs.dev/blog/biome-wins-prettier-challenge/https://biomejs.dev/blog/biome-wins-prettier-challenge/Biome formatter now 95% compatible with Prettier
Mon, 27 Nov 2023 00:00:00 GMT<p>With the release of Biome \*\*<code dir="auto">v1.4.0</code>
\*\*, we claim the bounty of the <a href="https://console.algora.io/challenges/prettier">Prettier challenge</a>!</p>
<p>With
<code dir="auto">v1.4.0</code>, you’ll get a better formatter experience, more formatting options, new VSCode features, new sponsors and more!</p>
<p>You can upgrade Biome by running the following command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@1.4.0</span></div></div><div><div><span>pnpm</span><span> </span><span>update</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@1.4.0</span></div></div><div><div><span>yarn</span><span> </span><span>upgrade</span><span> </span><span>--exact</span><span> </span><span>@biomejs/biome@1.4.0</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="better-formatter">Better formatter</h2></div>
<p>Biome formatter has now \*\*over 96% in terms of compatibility
\*\* against <a href="https://prettier.io/">Prettier</a>! This score is computed for JavaScript, TypeScript, and JSX formatting.</p>
<p>Merit of challenge that was launched by <a href="http://blog.vjeux.com/">Christopher Chedeau</a>, one of the Prettier’s creators.</p>
<p>The challenge attracted the attention of many people, and some of them decided to contribute to Biome to claim part of the bounty. I did see something amazing: contributors had an amazing coordination, they took ownership of the tasks and delivered the solution in a matter of hours.</p>
<p>I believe the main factors that made this possible are three:</p>
<ol>
<li>Money. It’s a fact, and it’s completely fine if someone decides to contribute only for earning a small stipend out of it.</li>
<li>Communication. We used <a href="https://github.com/biomejs/biome/issues/720">GitHub</a> as only medium of coordination. We provided information, instructions and help on how to deliver.</li>
<li>Infrastructure. Biome relies on a solid testing infrastructure, built by <a href="https://github.com/MichaReiser">previous</a> Rome Tools <a href="https://github.com/ematipico">employees</a> and <a href="https://github.com/IWANABETHATGUY/">contributors</a>. It’s able to catch every reformat bug, provide granular diffs and warn the user if the emitted output is the different from the one emitted by Prettier.</li>
</ol>
<p>Before the challenge, Biome had roughly a compatibility rate of 85%, based on our internal metrics (JavaScript, TypeScript and JSX, on options parity). Even though 85% might seem high, the impact of a low number such as 15% on big code bases is huge, and people might feel intimidated by so many changes, causing early adopters to receive frictions when bring Biome to their team. A member of our community shared some insights:</p>
<blockquote>
<p>As a great example of how much even just that last 5% has improved things for large codebases (and specifically with
<code dir="auto">bracketSpacing</code> and now <code dir="auto">bracketSameLine</code> implemented) i ran it one project in our monorepo […].</p>
<p>Just last week, this number
<code dir="auto">[diagnostics]</code> was more than 6,000. Even with the bracket options ignored, it was still more than 1000, and now there are only 200 left!</p>
</blockquote>
<p>Although the challenge is over, we are committed to improve even more the compatibility score with prettier. Any contribution in this regard is very welcome.</p>
<p>The challenge has also uncovered some cases in Prettier’s emitted output that we decided to not follow. We have created a <a href="https://biomejs.dev/formatter/differences-with-prettier">new section</a> in our website that explains them. Our hope is to make this section smaller with the time.</p>
<p>If there’s a divergence that isn’t documented in our website, you should consider that a bug and file an issue.</p>
<div><h4 id="new-formatting-options">New formatting options</h4></div>
<p>With this challenge, we added new options to the formatter:</p>
<ul>
<li>
<p><a href="https://biomejs.dev/reference/configuration#formatterlineending"><code dir="auto">lineEnding</code></a></p>
<p>Use this option to match the line endings of your OS. We support <code dir="auto">lf</code> (line feed - <code dir="auto">\n</code>), <code dir="auto">cr</code> (carriage return -
<code dir="auto">\r</code>) and <code dir="auto">crlf</code> (carriage return line feed - <code dir="auto">\r\n</code>).</p>
</li>
<li>
<p><a href="https://biomejs.dev/reference/configuration#javascriptormatterbracketsameline"><code dir="auto">bracketSameLine</code></a></p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>// Existing behavior. Now also the default, meaning `bracketSameLine: false`.</span></div></div><div><div><span>&#x3C;</span><span>Foo</span></div></div><div><div><span> </span><span>className</span><span>=</span><span>{</span><span>somethingReallyLongThatForcesThisToWrap</span><span>}</span></div></div><div><div><span> </span><span>anotherReallyLongAttribute</span><span>=</span><span>{</span><span>withAValueThatsSurelyTooLong</span><span>}</span></div></div><div><div><span> </span><span>soThatEverythingWraps</span></div></div><div><div><span>></span></div></div><div><div><span><span> </span></span><span>Hello</span></div></div><div><div><span>&#x3C;/</span><span>Foo</span><span>></span></div></div><div><div>
</div></div><div><div><span>&#x3C;</span><span>Foo</span></div></div><div><div><span> </span><span>selfClosingTags</span><span>=</span><span>{</span><span>likeThisOne</span><span>}</span></div></div><div><div><span> </span><span>stillPlaceTheBracket</span><span>=</span><span>{</span><span>onItsOwnLine</span><span>}</span></div></div><div><div><span> </span><span>toIndicateThat</span><span>=</span><span>{</span><span>itClosesItself</span><span>}</span></div></div><div><div><span>/></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>After formatting with <code dir="auto">"bracketSameLine": true</code>:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>// New behavior, with `bracketSameLine: true`.</span></div></div><div><div><span>&#x3C;</span><span>Foo</span></div></div><div><div><span> </span><span>className</span><span>=</span><span>{</span><span>somethingReallyLongThatForcesThisToWrap</span><span>}</span></div></div><div><div><span> </span><span>anotherReallyLongAttribute</span><span>=</span><span>{</span><span>withAValueThatsSurelyTooLong</span><span>}</span></div></div><div><div><span> </span><span>soThatEverythingWraps</span><span>></span></div></div><div><div><span><span> </span></span><span>Hello</span></div></div><div><div><span>&#x3C;/</span><span>Foo</span><span>></span></div></div><div><div>
</div></div><div><div><span>&#x3C;</span><span>Foo</span></div></div><div><div><span> </span><span>selfClosingTags</span><span>=</span><span>{</span><span>likeThisOne</span><span>}</span></div></div><div><div><span> </span><span>stillPlaceTheBracket</span><span>=</span><span>{</span><span>onItsOwnLine</span><span>}</span></div></div><div><div><span>/></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p><a href="https://biomejs.dev/reference/configuration#javascriptformatterbracketspacing"><code dir="auto">bracketSpacing</code></a></p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> { sort } </span><span>from</span><span> </span><span>"</span><span>sort.js</span><span>"</span><span>;</span></div></div><div><div><span>const </span><span>value</span><span> = { </span><span>sort</span><span> }</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>After formatting with <code dir="auto">"bracketSpacing": false</code>:</p>
<div><figure><figcaption><span>example.js</span></figcaption><pre><code><div><div><span>import</span><span> {sort} </span><span>from</span><span> </span><span>"</span><span>sort.js</span><span>"</span><span>;</span></div></div><div><div><span>const </span><span>value</span><span> = {</span><span>sort</span><span>}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
</ul>
<div><h2 id="vscode-extension-goodies">VSCode extension goodies</h2></div>
<p>The VSCode has been moved to a <a href="https://github.com/biomejs/biome-vscode">new repository</a>.</p>
<p>We removed the bundled binary from the extension, and you’ll be able to download the version that you want. Here’s a small video of how it works:</p>
<video width="1200" height="800" controls>
<source src="https://github.com/biomejs/biome-vscode/assets/649677/c7c1bf81-10a5-4cd6-bbdf-019d983a2d6a" type="video/mp4">
</video>
<p>From today, we release a <strong>nightly</strong> version of the extension.
This is a version meant for early adopters and to test things before they are officially released.</p>
<div><h2 id="some-cli-goodies">Some CLI goodies</h2></div>
<p>People that rely on Biome LSP will be pleased that they can now pass a custom configuration to the command
<code dir="auto">lsp-proxy</code>, using the option <code dir="auto">--config-path</code>. The same option is accepted by the command <code dir="auto">start</code>:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>--config-path=../path/where/config/is</span><span> </span><span>lsp-proxy</span></div></div><div><div><span>biome</span><span> </span><span>--config-path=../path/where/config/is</span><span> </span><span>start</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>The CLI now exposes the option <code dir="auto">--diagnostic-level</code>, that allows to filter the kind of diagnostics printed to terminal.</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>check</span><span> </span><span>--diagnostic-level=error</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="new-lint-rules-and-promoted-rule">New lint rules, and promoted rule</h2></div>
<p>Biome is a linter too, and it features <a href="https://biomejs.dev/linter/rules/">177 rules</a>! In this release, some rules are promoted and new ones are available.</p>
<div><h3 id="new-rules">New rules</h3></div>
<ul>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-default-export">noDefaultExport</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>export</span><span> </span><span>default</span><span> </span><span>function</span><span> </span><span>f</span><span>()</span><span> {}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noDefaultExport.js:1:8 <a href="https://biomejs.dev/linter/rules/no-default-export">lint/nursery/noDefaultExport</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>⚠</span></strong> <span>Avoid </span><span><strong>default</strong></span><span> exports.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>export default function f() {};
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Default exports cannot be easily discovered inside an editor and don't encourage the use of consistent names through a code base.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Use a named export instead.</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-aria-hidden-on-focusable">noAriaHiddenOnFocusable</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>div</span><span> </span></span><span>aria-hidden</span><span>=</span><span>"</span><span>true</span><span>"</span><span> </span><span>tabIndex</span><span>=</span><span>"</span><span>0</span><span>"</span><span> /></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noAriaHiddenOnFocusable.js:1:1 <a href="https://biomejs.dev/linter/rules/no-aria-hidden-on-focusable">lint/nursery/noAriaHiddenOnFocusable</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Disallow </span><span><strong>aria-hidden="true"</strong></span><span> from being set on focusable elements.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>&#x3C;div aria-hidden="true" tabIndex="0" />
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span><strong>aria-hidden</strong></span><span> should not be set to </span><span><strong>true</strong></span><span> on focusable elements because this can lead to confusing behavior for screen reader users.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Unsafe fix</span><span>: </span><span>Remove the aria-hidden attribute from the element.</span>
<strong> </strong><strong> 1 │ </strong>&#x3C;div<span>·</span><span>a</span><span>r</span><span>i</span><span>a</span><span>-</span><span>h</span><span>i</span><span>d</span><span>d</span><span>e</span><span>n</span><span>=</span><span>"</span><span>t</span><span>r</span><span>u</span><span>e</span><span>"</span><span><span>·</span></span>tabIndex="0"<span>·</span>/>
<strong> </strong><strong> │ </strong> <span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-implicit-any-let">noImplicitAnyLet</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>var </span><span>a;</span></div></div><div><div><span>a </span><span>=</span><span> </span><span>2</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/noImplicitAnyLet.js:1:5 <a href="https://biomejs.dev/linter/rules/no-implicit-any-let">lint/nursery/noImplicitAnyLet</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>This variable implicitly has the </span><span><strong>any</strong></span><span> type.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>var a;
<strong> │ </strong> <strong><span>^</span></strong>
<strong>2 │ </strong>a = 2;
<strong>3 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Variable declarations without type annotation and initialization have implicitly the </span><span><strong>any</strong></span><span> type. Declare type or initialize the variable with some value.</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-await">useAwait</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>async</span><span> </span><span>function</span><span> </span><span>fetchData</span><span>()</span><span> {</span></div></div><div><div><span> </span><span>// Missing `await` for the promise returned by `fetch`</span></div></div><div><div><span> </span><span>return</span><span> </span><span>fetch</span><span>(</span><span>"</span><span>/data</span><span>"</span><span>);</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useAwait.js:1:1 <a href="https://biomejs.dev/linter/rules/use-await">lint/nursery/useAwait</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>This </span><span><strong>async</strong></span><span> function lacks an </span><span><strong>await</strong></span><span> expression.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>async function fetchData() {
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong><span> </span></strong><strong><span>></span></strong> <strong>2 │ </strong>// Missing `await` for the promise returned by `fetch`
<strong><span> </span></strong><strong><span>></span></strong> <strong>3 │ </strong> return fetch('/data');
<strong><span> </span></strong><strong><span>></span></strong> <strong>4 │ </strong>}
<strong> │ </strong><strong><span>^</span></strong>
<strong>5 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Remove this </span><span><strong>async</strong></span><span> modifier, or add an </span><span><strong>await</strong></span><span> expression in the function.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>async function fetchData() {
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong><span> </span></strong><strong><span>></span></strong> <strong>2 │ </strong>// Missing `await` for the promise returned by `fetch`
<strong><span> </span></strong><strong><span>></span></strong> <strong>3 │ </strong> return fetch('/data');
<strong><span> </span></strong><strong><span>></span></strong> <strong>4 │ </strong>}
<strong> │ </strong><strong><span>^</span></strong>
<strong>5 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span><strong>Async</strong></span><span> functions without </span><span><strong>await</strong></span><span> expressions may not need to be declared </span><span><strong>async</strong></span><span>.</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-valid-aria-role">useValidAriaRole</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>div</span><span> </span></span><span>role</span><span>=</span><span>"</span><span>datepicker</span><span>"</span><span><span>>&#x3C;/</span><span>div</span><span>></span></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useValidAriaRole.js:1:1 <a href="https://biomejs.dev/linter/rules/use-valid-aria-role">lint/nursery/useValidAriaRole</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Enforce that elements with ARIA roles must use a valid, non-abstract ARIA role.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>&#x3C;div role="datepicker">&#x3C;/div>
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Check </span><span><a href="https://www.w3.org/TR/wai-aria/#namefromauthor">WAI-ARIA</a></span><span> for valid roles or provide options accordingly.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Unsafe fix</span><span>: </span><span>Remove the invalid </span><span><strong>role</strong></span><span> attribute.
</span><span> </span><span> </span><span> Check the list of all </span><span><a href="https://www.w3.org/TR/wai-aria/#role\_definitions">valid</a></span><span> role attributes.</span>
<strong> </strong><strong> 1 │ </strong>&#x3C;div<span>·</span><span>r</span><span>o</span><span>l</span><span>e</span><span>=</span><span>"</span><span>d</span><span>a</span><span>t</span><span>e</span><span>p</span><span>i</span><span>c</span><span>k</span><span>e</span><span>r</span><span>"</span>>&#x3C;/div>
<strong> </strong><strong> │ </strong> <span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-regex-literals">useRegexLiterals</a></p>
</li>
</ul>
<div><figure><figcaption></figcaption><pre><code><div><div><span>new</span><span> </span><span>RegExp</span><span>(</span><span>"</span><span>abc</span><span>"</span><span>, </span><span>"</span><span>u</span><span>"</span><span>);</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>nursery/useRegexLiterals.js:1:1 <a href="https://biomejs.dev/linter/rules/use-regex-literals">lint/nursery/useRegexLiterals</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>⚠</span></strong> <span>Use a regular expression literal instead of the </span><span><strong>RegExp</strong></span><span> constructor.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>new RegExp("abc", "u");
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Regular expression literals avoid some escaping required in a string literal, and are easier to analyze statically.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Safe fix</span><span>: </span><span>Use a </span><span><strong>literal notation</strong></span><span> instead.</span>
<strong>1</strong> <strong> │ </strong><span>-</span> <span><strong>n</strong></span><span><strong>e</strong></span><span><strong>w</strong></span><span><span><strong>·</strong></span></span><span><strong>R</strong></span><span><strong>e</strong></span><span><strong>g</strong></span><span><strong>E</strong></span><span><strong>x</strong></span><span><strong>p</strong></span><span><strong>(</strong></span><span><strong>"</strong></span><span>a</span><span>b</span><span>c</span><span><strong>"</strong></span><span><strong>,</strong></span><span><span><strong>·</strong></span></span><span><strong>"</strong></span><span>u</span><span><strong>"</strong></span><span><strong>)</strong></span><span>;</span>
<strong>1</strong><strong> │ </strong><span>+</span> <span><strong>/</strong></span><span>a</span><span>b</span><span>c</span><span><strong>/</strong></span><span>u</span><span>;</span>
<strong>2</strong> <strong>2</strong><strong> │ </strong>
</code></pre>
<div><h3 id="recommended-rules">Recommended rules</h3></div>
<ul>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-access-key">a11y/noAccessKey</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>input</span><span> </span></span><span>type</span><span>=</span><span>"</span><span>submit</span><span>"</span><span> </span><span>accessKey</span><span>=</span><span>"</span><span>s</span><span>"</span><span> </span><span>value</span><span>=</span><span>"</span><span>Submit</span><span>"</span><span> /></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>a11y/noAccessKey.js:1:22 <a href="https://biomejs.dev/linter/rules/no-access-key">lint/a11y/noAccessKey</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Avoid the </span><span><strong>accessKey</strong></span><span> attribute to reduce inconsistencies between keyboard shortcuts and screen reader keyboard comments.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>&#x3C;input type="submit" accessKey="s" value="Submit" />
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Assigning keyboard shortcuts using the </span><span><strong>accessKey</strong></span><span> attribute leads to inconsistent keyboard actions across applications.</span>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Unsafe fix</span><span>: </span><span>Remove the </span><span><strong>accessKey</strong></span><span> attribute.</span>
<strong> </strong><strong> 1 │ </strong>&#x3C;input<span>·</span>type="submit"<span>·</span><span>a</span><span>c</span><span>c</span><span>e</span><span>s</span><span>s</span><span>K</span><span>e</span><span>y</span><span>=</span><span>"</span><span>s</span><span>"</span><span><span>·</span></span>value="Submit"<span>·</span>/>
<strong> </strong><strong> │ </strong> <span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span><span>-</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-heading-content">a11y/useHeadingContent</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span><span>&#x3C;</span><span>h1</span><span> /></span></span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>a11y/useHeadingContent.js:1:1 <a href="https://biomejs.dev/linter/rules/use-heading-content">lint/a11y/useHeadingContent</a> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Provide screen reader accessible content when using </span><span><strong>heading</strong></span><span> elements.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>&#x3C;h1 />
<strong> │ </strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>All headings on a page should have content that is accessible to screen readers.</span>
</code></pre>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-simple-number-keys">complexity/useSimpleNumberKeys</a></p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>({ </span><span>0x1</span><span>: </span><span>1</span><span> });</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<pre><code>complexity/useSimpleNumberKeys.js:1:4 <a href="https://biomejs.dev/linter/rules/use-simple-number-keys">lint/complexity/useSimpleNumberKeys</a> <span> FIXABLE </span> ━━━━━━━━━━━━━━━━
<strong><span> </span></strong><strong><span>✖</span></strong> <span>Hexadecimal number literal is not allowed here.</span>
<strong><span> </span></strong><strong><span>></span></strong> <strong>1 │ </strong>({ 0x1: 1 });
<strong> │ </strong> <strong><span>^</span></strong><strong><span>^</span></strong><strong><span>^</span></strong>
<strong>2 │ </strong>
<strong><span> </span></strong><strong><span>ℹ</span></strong> <span>Safe fix</span><span>: </span><span>Replace 0x1 with 1</span>
<strong>1</strong> <strong> │ </strong><span>-</span> <span>(</span><span>{</span><span><span>·</span></span><span><strong>0</strong></span><span><strong>x</strong></span><span><strong>1</strong></span><span>:</span><span><span>·</span></span><span>1</span><span><span>·</span></span><span>}</span><span>)</span><span>;</span>
<strong>1</strong><strong> │ </strong><span>+</span> <span>(</span><span>{</span><span><span>·</span></span><span><strong>1</strong></span><span>:</span><span><span>·</span></span><span>1</span><span><span>·</span></span><span>}</span><span>)</span><span>;</span>
<strong>2</strong> <strong>2</strong><strong> │ </strong>
</code></pre>
</li>
</ul>
<div><h3 id="promoted-rules">Promoted rules</h3></div>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-interactive-element-to-noninteractive-role">a11y/noInteractiveElementToNoninteractiveRole</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-this-in-static">complexity/noThisInStatic</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-arrow-function">complexity/useArrowFunction</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-empty-character-class-in-regex">correctness/noEmptyCharacterClassInRegex</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-invalid-new-builtin">correctness/noInvalidNewBuiltin</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-else">style/noUselessElse</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-as-const-assertion">style/useAsConstAssertion</a></li>
<li><a href="https://biomejs.dev/linter/rules/use-shorthand-assign">style/useShorthandAssign</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-approximative-numeric-constant">suspicious/noApproximativeNumericConstant</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misleading-instantiator">suspicious/noMisleadingInstantiator</a></li>
<li><a href="https://biomejs.dev/linter/rules/no-misrefactored-shorthand-assign">suspicious/noMisrefactoredShorthandAssign</a></li>
</ul>
<div><h3 id="deprecated-rules">Deprecated rules</h3></div>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-new-symbol">correctness/noNewSymbol</a></li>
</ul>
<p>The rule is replaced by <a href="https://biomejs.dev/linter/rules/no-invalid-new-builtin">correctness/noInvalidNewBuiltin</a></p>
<div><h2 id="homage-to-our-maintainers">Homage to our maintainers</h2></div>
<p>Since Biome was forked, new people joined the project. They have been helping with in so many ways that you can’t even imagine: new features, side projects, engaging with the community, support, documentation, and more. OSS is not just about coding.</p>
<p>Thank you to:</p>
<ul>
<li><a href="https://github.com/SuperchupuDev">Madeline Gurriarán @SuperchupuDev</a></li>
<li><a href="https://github.com/nhedger">Nicolas Hedger @nhedger</a></li>
<li><a href="https://github.com/victor-teles">Victor Teles @victor-teles</a></li>
</ul>
<p>And a big welcome to our new joined maintainer:</p>
<ul>
<li><a href="https://github.com/faultyserver">Jon Egeland @faultyserver</a></li>
<li><a href="https://github.com/TaKO8Ki">Takayuki Maeda @TaKO8Ki</a></li>
</ul>
<div><h2 id="new-sponsors">New sponsors</h2></div>
<p>Last but not least, we are proud to announce that we have two new sponsors:</p>
<ul>
<li>Gold: Shiguredō (<a href="https://shiguredo.jp/">https://shiguredo.jp/</a>)</li>
<li>Bronze: KANAME (<a href="https://www.kanamekey.com/">https://www.kanamekey.com/</a>)</li>
</ul>
<div><h2 id="whats-next">What’s next</h2></div>
<p>The project is thriving, with more people curious about the project and contributors that want to be involved.</p>
<p>In the next months we will focus on:</p>
<ul>
<li>Publishing a Roadmap. <strong>Keep an eye on it</strong>, it will involve a lot of <strong>interesting</strong> work.</li>
<li>Rebranding the website with a new logo.</li>
<li>Translate the website in Japanese.</li>
</ul>
<div><h2 id="translations">Translations</h2></div>
<ul>
<li><a href="https://juejin.cn/post/7308643782375768118">中文翻译: Biome赢得了Prettier挑战</a></li>
</ul>Announcing Biomehttps://biomejs.dev/blog/announcing-biome/https://biomejs.dev/blog/announcing-biome/Biome continues Rome's legacy; in this blog post, we explain why the fork, with some context and history.
Tue, 29 Aug 2023 00:00:00 GMT<p>We are happy to announce Biome, <em>toolchain of the web</em>.</p>
<p>Biome is the <strong>official</strong> fork of Rome and it will continue to be Rome’s legacy.</p>
<p>Biome is <strong>led and maintained</strong> by the same people that maintained Rome so far.</p>
<p><strong>Follow us</strong>:</p>
<ul>
<li><a href="https://github.com/biomejs">Github organization</a></li>
<li><a href="https://github.com/biomejs/biome">Official repository</a></li>
<li><a href="https://biomejs.dev/chat">Official discord server</a></li>
</ul>
<div><h2 id="background">Background</h2></div>
<p>I want to give you some background and context, which could help you to get why the core team created a new project with a new name. If you’re not interested, feel free to jump to the <a href="#enters-biome">next section</a></p>
<div><h3 id="how-it-started">How it started</h3></div>
<p>Before explaining the reasons for the fork, I’d like to give you some background and context; this would help you understand the reasons
that led to this decision.</p>
<p>When I <a href="https://github.com/rome/tools/pull/794">joined</a> the Rome project, the project was still young and written in <a href="https://github.com/rome/tools/tree/archived-js">TypeScript</a>.
A long time passed, and the project underwent many transitions.</p>
<p>Rome was initially released and licensed under the Meta OSS umbrella. Meta is an excellent incubator for OSS projects, but some people didn’t like it. At least, my impression was that they didn’t.</p>
<p>The npm package <code dir="auto">rome</code> belonged to another person, so when ownership changed, there were already a lot of version numbers used. The team always struggled with versioning. It shouldn’t be hard to version a software!</p>
<p>After a few months, the project got out of Meta’s OSS umbrella. In six months, the creator Sebastian McKenzie created the company Rome Tools Inc., to keep working on the Rome project so to eventually became sustainable.</p>
<p>I was excited about the news because I believed in Rome’s mission, so I decided to quit my job and join the adventure. In a few weeks, I joined Rome Tools Inc. as
a full-time employee to work on developer tools as my daily job. For me, it was like a dream coming true!</p>
<div><h3 id="how-it-ended-or-did-it">How it ended (or did it?)</h3></div>
<p>Not all startups manage to succeed, and Rome Tools Inc. wasn’t one of the lucky ones. Eventually, all the employees were laid off.</p>
<p>My adventure with Rome Tools Inc. sadly ended, but fortunately, my career working with developer tools continued! A few months later, I joined the <a href="https://astro.build/">Astro Technology Company</a> working full-time. It’s a great place to work, and I get to do what I love every day with fantastic people. I love it!</p>
<p>Part of me was still charmed by Rome’s mission though. However, it wasn’t just that. I like working on parsers/compilers in my free time. I <strong>love</strong> the <a href="https://www.rust-lang.org/">Rust</a> language, and Rome is the perfect OSS project where I can use it.</p>
<p>So, in my free time, I continued with my contributions to Rome as much as possible; luckily, I still had some rights that allowed me to publish new versions of the project. Despite the unsuccessful adventure with Rome Tools Inc., I wanted to keep the project alive.</p>
<p>A few new <a href="#the-core-team">OSS contributors</a> joined the cause and helped in contributing to the project. I wasn’t alone, and that’s the great thing about OSS. You eventually find people who like the project and want to contribute too.</p>
<p>In June, I <a href="https://portal.gitnation.org/contents/rome-a-modern-toolchain">gave a talk</a> about Rome at JsNation 2023.</p>
<p><img src="https://biomejs.dev/\_astro/JsNation\_2023.Bny4KZ09\_mt3PT.webp?dpl=69dce24b554af000071740e1" alt="Emanuele Stoppa on the stage of JsNation" loading="lazy" decoding="async" fetchpriority="auto" width="2048" height="1365"></p>
<p>So, the project is still alive, but maintaining it has become challenging:</p>
<ul>
<li>I don’t have admin rights on Discord, so I can’t delegate moderation rights to other people;</li>
<li>I don’t have access to the hosting platform of the website;</li>
<li>I don’t have access to any registry (npm, VSCode, etc.);</li>
<li>the project is still under the MIT license of Rome Tools Inc., which makes attributions and contributions seem foggy from a legal point of view (where’s the company? I don’t know).</li>
</ul>
<p>Many attempts to reach out to the current owner were all void. There was only one thing I could do. <strong><a href="#the-core-team">We could do</a>.</strong></p>
<div><h2 id="enters-biome">Enters: Biome</h2></div>
<p>We created Biome. After weeks of discussions among the members of the core team and conversations with some friends, we thought that a clean slate was the best course of action.</p>
<p>We pondered the idea of keeping the “rome” name in the new fork, but that was proven difficult:</p>
<ul>
<li>Sebastian has registered tons of stuff with the “rome” name (GitHub organizations, website domains, open collectives, npm organizations). Finding the right combination wasn’t easy;</li>
<li>without the proper rights in the Discord server, we couldn’t delegate the moderation rights. Discord is a very important asset for community building;</li>
<li>keeping the name would have caused some attribution to Rome Tools Inc., making things still foggy when it comes to the legal aspects of the source code;</li>
<li>we don’t know if the “rome” name is registered; if it turns out it is, we could have incurred some legal troubles;</li>
<li>“Rome” has a lot of historical baggage, as explained before (Meta and, fail as a startup);</li>
</ul>
<p>Given all these difficulties, the core team settled for a new project.</p>
<div><h3 id="new-is-always-better">”New is always better.”</h3></div>
<div><img src="https://media.giphy.com/media/7EamSGumESd0Y/giphy.gif" width="100%"></div>
<p>Biome will embrace the same <a href="https://biomejs.dev/internals/philosophy">philosophy</a> of the old Rome and the same mission. Although, the roadmap will likely change, and the core team could decide to focus on making the current features more stable instead of releasing new ones.</p>
<p>Still, the primary mission is alive, and Biome wants to be a 360° toolchain; we recently started working on <strong>transformations</strong>, which will eventually set up the foundations of the compiler.</p>
<div><h3 id="why-biome">Why Biome</h3></div>
<p>The team wanted to create a second “Rome”, a second version of it. So we fused the words “Bis” and “Rome”. \*\*Biome"".</p>
<div><h2 id="i-still-use-the-rome-package-what-should-i-do">I still use the <code dir="auto">rome</code> package. What should I do?</h2></div>
<p>The <code dir="auto">rome</code> package <strong><em>won’t be maintained anymore</em></strong> by the core team, so you won’t get any more releases.</p>
<ol>
<li>
<p>You should use the <code dir="auto">@biomejs/biome</code> package. Note that Biome also comes with a lot of new features and fixes. We’ve just prepared a <a href="https://biomejs.dev/blog/biome-v1">blog post</a> for that.</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span><span> </span></span><span>"rome": "12.1.3"</span></div></div><div><div><span><span> </span></span><span>"@biomejs/biome": "1.0.0"</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>And change the CLI name in your scripts:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span><span> </span></span><span>"scripts": {</span></div></div><div><div><span><span> </span></span><span>"format": "rome format --write ./src",</span></div></div><div><div><span><span> </span></span><span>"format": "biome format --write ./src"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>In your <code dir="auto">rome.json</code> file, update the URL of the <code dir="auto">$schema</code> field:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span><span> </span></span><span>"$schema": "https://docs.rome.tools/schemas/12.1.3/schema.json",</span></div></div><div><div><span><span> </span></span><span>"$schema": "https://biomejs.dev/schemas/1.0.0/schema.json"</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
<li>
<p>Then install the new official <a href="https://marketplace.visualstudio.com/items?itemName=biomejs.biome">VSCode</a> or <a href="https://open-vsx.org/extension/biomejs/biome">open VSX</a> extension. That’s an important step if you use these extensions.</p>
</li>
<li>
<p>After the installation of the extension, open the <code dir="auto">settings.json</code>. If you have some Rome related settings there, you’ll have to update them:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span><span> </span></span><span>"[javascript]": {</span></div></div><div><div><span><span> </span></span><span>"editor.defaultFormatter": "rome.rome"</span></div></div><div><div><span><span> </span></span><span>"editor.defaultFormatter": "biomejs.biome"</span></div></div><div><div><span><span> </span></span><span>},</span></div></div><div><div><span><span> </span></span><span>"editor.codeActionsOnSave": {</span></div></div><div><div><span><span> </span></span><span>"quickfix.rome": true,</span></div></div><div><div><span><span> </span></span><span>"source.organizeImports.rome": true</span></div></div><div><div><span><span> </span></span><span>"quickfix.biome": true,</span></div></div><div><div><span><span> </span></span><span>"source.organizeImports.biome": true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
</li>
</ol>
<p>Biome <strong>still accepts the <code dir="auto">rome.json</code> file</strong> as a configuration, so you don’t need to do anything yet. Biome also takes <code dir="auto">biome.json</code> as a configuration file.</p>
<p>We will eventually sunset the <code dir="auto">rome.json</code> configuration file for <code dir="auto">biome.json</code>, but Biome will do that for you in the subsequent releases. So, don’t worry about updating everything unless you want to.</p>
<div><h2 id="the-core-team">The core team</h2></div>
<ul>
<li><a href="https://github.com/ematipico">Emanuele Stoppa</a>: me, the lead of the project 🤓</li>
<li><a href="https://github.com/denbezrukov">Denis Bezrukov</a>: Denis has contributed to the project for a long time He made contributions to many tools like formatter and parser;</li>
<li><a href="https://github.com/Conaclos">Victorien Elvinger</a>: Victorien is very passionate, and he’s made tons of contributions to the Biome linter by creating new rules and optimising the ones that were already there when he joined;</li>
<li><a href="https://github.com/nissy-dev">Daiki Nishikawa</a>: Daiki worked on linter and parser, by adding new rules, fixing the existing ones, improving the internal semantic model, and adding new grammar to the JavaScript/TypeScript parser;</li>
<li><a href="https://github.com/unvalley">unvalley</a>: unvalley added a lot of value to the linter and parser. They tackled some complex rules, for example, especially the ones around regex;</li>
</ul>
<div><h2 id="special-thanks">Special thanks</h2></div>
<ul>
<li><a href="https://github.com/strager">Strager</a>: his inputs and constructive criticisms to the project are what helped Biome to arrive to this point;</li>
<li><a href="https://github.com/Boshen">Boshen</a>: one of the greatest admirers of the project since the Rust rewrite; he joined the Biome community to learn from us and contribute as much as possible. He now leads a similar project to Biome, <a href="https://github.com/web-infra-dev/oxc">oxc</a>. Check it out.</li>
<li><a href="https://github.com/MichaReiser">Micha</a>: ex-employee of Rome Tools Inc., he is now a full-time developer of the project <a href="https://github.com/astral-sh/ruff">Ruff</a>, he gave a lot of good pieces of advice, and he was a good listener when I was struggling to make the right decisions.</li>
</ul>
<div><h2 id="translations">Translations</h2></div>
<ul>
<li><a href="https://juejin.cn/post/7308539123538608165">中文翻译: 宣布 Biome</a></li>
</ul>Biome v1https://biomejs.dev/blog/biome-v1/https://biomejs.dev/blog/biome-v1/New formatter options, CLI improvements, JSONC support and more.
Tue, 29 Aug 2023 00:00:00 GMT<p>In Biome v1, the formatter has options for JSX quotes and parentheses in the arrow functions; the CLI adds a new command <code dir="auto">biome lint</code>, <code dir="auto">.jsonc</code> files are supported, and it’s possible to extend the configuration file.</p>
<p>You can upgrade Biome by running the following command:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>npm</span><span> </span><span>install</span><span> </span><span>--save-dev</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@1.0.0</span></div></div><div><div><span>pnpm</span><span> </span><span>update</span><span> </span><span>--save-exact</span><span> </span><span>@biomejs/biome@1.0.0</span></div></div><div><div><span>yarn</span><span> </span><span>upgrade</span><span> </span><span>--exact</span><span> </span><span>@biomejs/biome@1.0.0</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Or install the <a href="https://marketplace.visualstudio.com/items?itemName=biomejs.biome">VS Code extension</a> to integrate Biome into your editor.</p>
<div><h2 id="new-formatter-options">New formatter options</h2></div>
<p>Biome now supports two new, long-awaited options:</p>
<ul>
<li>support for formatting the preferred quote kind in JSX;</li>
<li>support for formatting parenthesis in arrow functions only when they are needed;</li>
</ul>
<div><h3 id="jsx-quotes-style">JSX quotes style</h3></div>
<p>You can use this option via CLI or via <code dir="auto">biome.json</code> file:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"jsxQuoteStyle"</span><span>: </span><span>"</span><span>single</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--jsx-quote-style=single</span><span> </span><span>--write</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>And Biome will apply single quotes when defining attributes in JSX code:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>import</span><span> Item </span><span>from</span><span> </span><span>"</span><span>./item.jsx</span><span>"</span><span>;</span></div></div><div><div>
</div></div><div><div><span>const </span><span>Header</span><span> = </span><span>()</span><span> => {</span></div></div><div><div><span><span> </span></span><span>return </span><span>&#x3C;</span><span>Item</span><span> </span><span>title</span><span>=</span><span>"</span><span>Docs</span><span>"</span><span><span> /></span><span>;</span></span></div></div><div><div><span>}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="arrow-function-parenthesis">Arrow function parenthesis</h3></div>
<p>You can decide not to print parenthesis in arrow functions. You can customize the option via CLI or via <code dir="auto">biome.json</code>:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"formatter"</span><span>: {</span></div></div><div><div><span> </span><span>"arrowParentheses"</span><span>: </span><span>"</span><span>asNeeded</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>format</span><span> </span><span>--arrow-parentheses=as-needed</span><span> </span><span>--write</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>And Biome will print parenthesis only for those arrow functions that require them:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>// no need for parentheses</span></div></div><div><div><span>const </span><span>filter</span><span> = </span><span>(</span><span>term</span><span>)</span><span> => {}</span><span>;</span></div></div><div><div><span>// needs parentheses</span></div></div><div><div><span>const </span><span>filterBy</span><span> = </span><span>(</span><span>term</span><span>, </span><span>fn</span><span>)</span><span> => {}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="cli-improvements">CLI improvements</h2></div>
<p>The CLI was heavily reworked to guarantee consistent behaviour when handling files, diagnostics emitted and commands.</p>
<p>Among those changes, there are some <strong>breaking changes</strong> in its behaviour.</p>
<ul>
<li>The CLI exits with an error code if the configuration file contains errors; while Biome can parse the configuration successfully - even with errors - this was a hazard for our users.
A typo in the configuration file would have resulted in Biome applying its defaults, and executing Biome with a different behaviour compared to the one set by the user.</li>
<li>The command <code dir="auto">biome check</code> will now emit error diagnostics for <em>code not formatted</em> and exits with an error code. This behaviour aligns with the semantics meant for this command.</li>
</ul>
<div><h3 id="new-biome-lint-command">New <code dir="auto">biome lint</code> command</h3></div>
<p>The command <code dir="auto">biome check</code> is meant to run multiple tools, which sometimes can overwhelm the users. With <code dir="auto">biome lint</code>, Biome will only run lint rules against files.</p>
<p>As for now, the command accepts almost all the CLI arguments of the <code dir="auto">biome check</code>. In the future, this command will specialize and tweak its behaviour around linting.</p>
<div><h3 id="more-control-over-errors">More control over errors</h3></div>
<p>By default, when Biome sees a file that can’t handle, it fires a diagnostic and will exit with an error code.</p>
<p>With <code dir="auto">--files-ignore-unknown</code> option, the CLI won’t emit diagnostics and will continue processing files.</p>
<p>You can define this behaviour in the <code dir="auto">biome.json</code> too:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"files"</span><span>: {</span></div></div><div><div><span> </span><span>"ignoreUnknown"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>When Biome doesn’t process files during a command, it exits with an error code and emits an error diagnostic.</p>
<p>Now, with <code dir="auto">--no-errors-on-unmatched</code>, Biome will exist with a successful code and doesn’t emit any diagnostics.</p>
<p>This new option allows users to use Biome with tools like <code dir="auto">lint-staged</code>.</p>
<div><h3 id="exit-on-warnings">Exit on warnings</h3></div>
<p>In Biome, you can change the configuration of rules and allow them to emit diagnostics. This behaviour was limited, and now with <code dir="auto">--error-on-warnings</code> option, you can tell Biome to exit with an error code if a <strong>warning</strong> is emitted.</p>
<p>Here’s an example, let’s change the diagnostic level of a rule via <code dir="auto">biome.json</code>:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"linter"</span><span>: {</span></div></div><div><div><span> </span><span>"recommended"</span><span>: </span><span>true</span><span>,</span></div></div><div><div><span> </span><span>"rules"</span><span>: {</span></div></div><div><div><span> </span><span>"a11y"</span><span>: {</span></div></div><div><div><span> </span><span>"useAltText"</span><span>: </span><span>"</span><span>warn</span><span>"</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Here’s a sample code that will trigger the rule:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>const </span><span>Image</span><span> = </span><span>()</span><span> => {</span></div></div><div><div><span><span> </span></span><span>return </span><span>&#x3C;</span><span>img</span><span> </span><span>src</span><span>=</span><span>"</span><span>https://example.com/image.png</span><span>"</span><span><span> /></span><span>;</span></span></div></div><div><div><span>}</span><span>;</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>And now, run the CLI using the new option:</p>
<div><figure><figcaption><span></span></figcaption><pre><code><div><div><span>biome</span><span> </span><span>lint</span><span> </span><span>--error-on-warnings</span><span> </span><span>./src</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h2 id="jsonc-support-and-comments">JSONC support and comments</h2></div>
<p>Biome’s JSON parser now supports comments, so we enabled these exciting new features.</p>
<div><h3 id="jsonc-file-support"><code dir="auto">.jsonc</code> file support</h3></div>
<p>Biome can now format and lint <code dir="auto">.jsonc</code> files.</p>
<div><h3 id="allow-comments-in-json-files">Allow comments in JSON files</h3></div>
<p>Biome can parse comments inside JSON files. You can opt-in to this feature via the configuration file:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"json"</span><span>: {</span></div></div><div><div><span> </span><span>"parser"</span><span>: {</span></div></div><div><div><span> </span><span>"allowComments"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<aside aria-label="Note"><p aria-hidden="true">Note</p><div><p>The <code dir="auto">biome.json</code> file <strong>doesn’t</strong> allow comments.</p></div></aside>
<aside aria-label="Caution"><p aria-hidden="true">Caution</p><div><p>When enabling this feature, comments will be permitted in <strong>all</strong> JSON files encountered by Biome.</p></div></aside>
<p>Plus, Biome now recognizes some <strong>known</strong> files as “JSON files that can have comments”. For example, now Biome can
format your <code dir="auto">tsconfig.json</code> file with comments without emitting errors!</p>
<div><h2 id="extends-property"><code dir="auto">extends</code> property</h2></div>
<p>You can now break down your configuration file into different files and join them using the new <code dir="auto">extends</code> property.</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"extends"</span><span>: [</span><span>"</span><span>./formatter.json</span><span>"</span><span>, </span><span>"</span><span>./linter.json</span><span>"</span><span>]</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Check the <a href="https://biomejs.dev/reference/configuration#extends">documentation</a> to understand how it works.</p>
<div><h2 id="linter">Linter</h2></div>
<p>We <strong>deleted</strong> two rules:</p>
<ul>
<li><code dir="auto">useCamelCase</code>, which is replaced by <code dir="auto">useNamingConvention</code>;</li>
<li><code dir="auto">noExtraSemicolon</code>, not needed; the formatter takes care of it;</li>
</ul>
<div><h3 id="new-rules">New Rules</h3></div>
<ul>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-duplicate-json-keys/"><code dir="auto">noDuplicateJsonKeys</code></a></p>
<p>This rule disallows duplicate keys in a JSON object.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-excessive-cognitive-complexity/"><code dir="auto">noExcessiveComplexity</code></a></p>
<p>This rule computes a complexity score and reports code with a score above a configurable threshold.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-fallthrough-switch-clause/"><code dir="auto">noFallthroughSwitchClause</code></a></p>
<p>This rule disallows <code dir="auto">switch</code> cases that fall through to the next <code dir="auto">case</code>.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-global-is-finite/"><code dir="auto">noGlobalIsFinite</code></a></p>
<p>This rule recommends using <code dir="auto">Number.isFinite</code> instead of the global and unsafe <code dir="auto">isFinite</code> that attempts a type of coercion.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-global-is-nan/"><code dir="auto">noGlobalIsNan</code></a></p>
<p>This rule recommends using <code dir="auto">Number.isNaN</code> instead of the global and unsafe <code dir="auto">isNaN</code> that attempts a type of coercion.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-nonoctal-decimal-escape/"><code dir="auto">noNonoctalDecimalEscape</code></a></p>
<p>This rule disallows <code dir="auto">\8</code> and <code dir="auto">\9</code> escape sequences in string literals.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-unsafe-declaration-merging/"><code dir="auto">noUnsafeDeclarationMerging</code></a></p>
<p>This rule disallows declaration merging between an interface and a class.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-useless-empty-export/"><code dir="auto">noUselessEmptyExport</code></a></p>
<p>This rule disallows useless <code dir="auto">export {}</code>.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-useless-this-alias/">noUselessThisAlias</a></p>
<p>This rule disallows useless aliasing of <code dir="auto">this</code> in arrow functions.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/no-void/"><code dir="auto">noVoid</code></a></p>
<p>This rule disallows the use of <code dir="auto">void</code>.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-arrow-function/"><code dir="auto">useArrowFunction</code></a></p>
<p>This rule proposes turning function expressions into arrow functions.
Function expressions that use <code dir="auto">this</code> are ignored.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-getter-return/"><code dir="auto">useGetterReturn</code></a></p>
<p>This rule enforces <code dir="auto">get</code> methods to always return a value.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-import-restrictions/"><code dir="auto">useImportRestrictions</code></a></p>
<p>Enables restrictions on how local imports should be imported.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-is-array/"><code dir="auto">useIsArray</code></a></p>
<p>This rule proposes using <code dir="auto">Array.isArray()</code> instead of <code dir="auto">instanceof Array</code>.</p>
</li>
<li>
<p><a href="https://biomejs.dev/linter/rules/use-naming-convention/"><code dir="auto">useNamingConvention</code></a></p>
<p>The rule enforces wide-spread naming conventions of Javascript and TypeScript across a codebase.</p>
</li>
</ul>
<div><h4 id="promoted-rules">Promoted rules</h4></div>
<p>New rules are promoted, please check <a href="https://github.com/rome/tools/discussions/4750">#4750</a> for more details:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/no-duplicate-jsx-props/"><code dir="auto">suspicious/noDuplicateJsxProps</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-console-log/"><code dir="auto">suspicious/noConsoleLog</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-is-nan/"><code dir="auto">correctness/useIsNan</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-simple-number-keys/"><code dir="auto">complexity/useSimpleNumberKeys</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-literal-keys/"><code dir="auto">complexity/useLiteralKeys</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-for-each/"><code dir="auto">complexity/noForEach</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/use-heading-content/"><code dir="auto">a11y/useHeadingContent</code></a></li>
</ul>
<p>The following rules are now recommended:</p>
<ul>
<li><a href="https://biomejs.dev/linter/rules/use-exponentiation-operator/"><code dir="auto">useExponentiationOperator</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-useless-fragments/"><code dir="auto">noUselessFragments</code></a></li>
<li><a href="https://biomejs.dev/linter/rules/no-redundant-use-strict/"><code dir="auto">noRedundantUseStrict</code></a></li>
</ul>
<div><h2 id="support-for-function-class-parameter-decorators">Support for function class parameter decorators</h2></div>
<p>In the last release, Biome introduced support for Stage 3 decorators. Although, this final proposal doesn’t support the function class parameter decorators:</p>
<div><figure><figcaption></figcaption><pre><code><div><div><span>class</span><span> </span><span>Controller</span><span> {</span></div></div><div><div><span> </span><span>get</span><span>(</span><span>@</span><span>Param</span><span>(</span><span>"</span><span>id</span><span>"</span><span><span>) </span><span>id</span></span><span>:</span><span> </span><span>string</span><span>)</span><span> {}</span></div></div><div><div><span> </span><span>// ^^^^^^^^^^^^ syntax not covered by the official and final decorators spec</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<p>Some users were dissatisfied because they couldn’t use Biome inside their Angular/NestJS project. Now you can do it via configuration:</p>
<div><figure><figcaption><span>biome.json</span></figcaption><pre><code><div><div><span>{</span></div></div><div><div><span> </span><span>"javascript"</span><span>: {</span></div></div><div><div><span> </span><span>"parser"</span><span>: {</span></div></div><div><div><span> </span><span>"unsafeParameterDecoratorsEnabled"</span><span>: </span><span>true</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span><span> </span></span><span>}</span></div></div><div><div><span>}</span></div></div></code></pre><div><div aria-live="polite"></div></div></figure></div>
<div><h3 id="acknowledgements">Acknowledgements</h3></div>
<p>Big thank you to the following contributors:</p>
<ul>
<li><a href="https://github.com/denbezrukov">denbezrukov</a>, they implemented the new decorator parameter, the new option <code dir="auto">jsxQuoteStyle</code> in the formatter, and started the works for our new CSS parser;</li>
<li><a href="https://github.com/Conaclos">Conaclos</a>, they continued creating new rules, making the existing ones smarter and adding tons of value to Biome;</li>
<li><a href="https://github.com/SuperchupuDev">SuperchupuDev</a>, they implemented the new option <code dir="auto">arrowParentheses</code> in the formatter;</li>
<li><a href="https://github.com/nissy-dev">nissy-dev</a>, they fixed a bunch of issues around the linter;</li>
<li><a href="https://github.com/unvalley">unvalley</a>, they fixed a bunch of issues around the linter and implemented new rules;</li>
<li><a href="https://github.com/arendjr">arendjr</a>, they implemented new rules in the linter and implemented the new import sorting strategy;</li>
<li><a href="https://github.com/ddanielsantos">ddanielsantos</a>, for their first contribution to the project;</li>
<li><a href="https://github.com/nikeee">nikeee</a>, for their first contribution to the project;</li>
</ul>
<div><h2 id="translations">Translations</h2></div>
<ul>
<li><a href="https://juejin.cn/post/7308539123538624549">中文翻译: Biome v1版本</a></li>
</ul>
