
<body>

<h1><strong>ContextforAIcoder</strong></h1>
<p><em>Readme.md was generated using OpenAI so if you see some errors please don’t get triggered!</em></p>
<p><em>IMP: you can also use it with your existing project just tell your ai code helper to make changes to your files as per .cursorrules and then you can manually decide which changes you want and this way watcher will be called and it will update vector database too for updated context which you can later reference with your ai code helper.</em></p>

<p>This repository provides a <strong>“Meta/Context” system</strong> for advanced AI-driven development. It includes:</p>
<ul>
    <li>Templates for <code>.cursorrules</code> (AI code style/documentation rules) and <code>PROJECT_CONTEXT.json</code> (project details).</li>
    <li>Automation Scripts to watch for code changes and automatically update a local vector database (Chroma) with new embeddings, enabling semantic search via LangChain.</li>
    <li>Guidelines for integrating these meta-features with your IDE (e.g., Cursor), ChatGPT, or local Large Language Models (LLMs).</li>
</ul>

<hr />

<h2><strong>Directory Structure</strong></h2>
<pre class="code-block"><code>ContextforAIcoder/
├── context/
│   ├── PROJECT_CONTEXT.template.json
│   ├── cursorrules.template.json
│   └── watchers/
│       ├── watch_changes.py
│       └── update_embeddings.py
├── README.md
├── .gitignore
└── ...
</code></pre>

<hr />

<h3><strong>What’s Inside</strong></h3>
<ul>
  <li>
    <strong>PROJECT_CONTEXT.template.json</strong><br />
    A base JSON template for storing high-level project metadata (name, description, features, tech stack, etc.). 
    Copy or rename it to <code>PROJECT_CONTEXT.json</code> in your actual project.
  </li>
  
  <li>
    <strong>cursorrules.template.json</strong><br />
    A template defining code documentation/style rules for AI tools. 
    Rename/copy to <code>.cursorrules</code> (or <code>cursorrules.json</code>) 
    in your target project so your IDE/AI sees it.
  </li>

  <li>
    <strong>watch_changes.py</strong><br />
    A Python script using <strong>Watchdog</strong> to monitor file changes in real time. 
    Whenever a watched file changes, it calls <code>update_embeddings.py</code> to re-embed that file.
  </li>

  <li>
    <strong>update_embeddings.py</strong><br />
    A Python script that uses <strong>LangChain</strong> + <strong>Chroma</strong> to embed 
    the contents of changed files into a local vector database. 
    This enables semantic search or advanced AI workflows.
  </li>
</ul>

<hr />

<h2><strong>Requirements</strong></h2>
<ol>
    <li><strong>Python 3.8+</strong><br />
        <em>For running the watchers and embedding scripts.</em>
    </li>
    <li><strong>Pip Packages</strong>:
        <pre class="code-block"><code>pip install watchdog langchain chromadb openai tiktoken</code></pre>
        <ul>
            <li><strong>Watchdog</strong>: For file system monitoring.</li>
            <li><strong>LangChain</strong>: For embedding and searching documents.</li>
            <li><strong>Chroma</strong> (in <code>chromadb</code>): Local vector store.</li>
            <li><strong>OpenAI / tiktoken</strong>: If using OpenAI embeddings.</li>
            <li>(You can swap out <code>OpenAIEmbeddings</code> with <code>HuggingFaceEmbeddings</code> if you prefer local embeddings.)</li>
        </ul>
    </li>
    <li><strong>Git</strong> (optional but recommended)<br />
    If you want to use Git hooks or submodule approach.</li>
</ol>

<hr />

<h2><strong>Setup</strong></h2>
<ol>
  <li>
    <strong>Clone this Repo</strong>
    <pre class="code-block"><code>git clone https://github.com/specifiedcodes/ContextforAIcoder.git</code></pre>
  </li>

  <li>
    <strong>(Optional) Add a <code>.gitignore</code></strong><br />
    Make sure your local embeddings directory (<code>.chroma/</code> or <code>db/</code>) is ignored to avoid committing large files.
  </li>
</ol>

<hr />

<h2><strong>Usage</strong></h2>
<h3><strong>A. Embedding Code &amp; Docs</strong></h3>

<ol>
  <li>
    <strong>Run <code>update_embeddings.py</code> Directly</strong><br />
    <p>(In the default example, it tries to embed <code>["src/routes/user.js", "README.md"]</code>. Adapt it to your own file paths.)</p>
    <pre class="code-block"><code>cd context/watchers
python update_embeddings.py
</code></pre>
  </li>

  <li>
    <strong>Run the Watcher Script (<code>watch_changes.py</code>)</strong><br />
    <p>In <code>context/watchers/</code>:</p>
    <pre class="code-block"><code>python watch_changes.py</code></pre>
    <p>
      This script will watch for changes in your project (by default the current directory) and 
      automatically call <code>update_embeddings.py &lt;filepath&gt;</code> each time a relevant file changes.<br />
      Modify the <code>TARGET_EXTENSIONS</code> list inside 
      <code>watch_changes.py</code> to match the file types you want to embed (<code>.js</code>, <code>.py</code>, 
      <code>.cs</code>, <code>.md</code>, etc.).
    </p>
  </li>
</ol>

<p><strong>Where Are the Embeddings Saved?</strong><br />
By default, Chroma will create a local DB folder (often <code>.chroma/</code>) in your working directory.<br />
You can customize this in <code>update_embeddings.py</code> (e.g., <code>db = Chroma(collection_name="my-project", persist_directory="my_chroma_db")</code>).
</p>

<hr />

<h3><strong>B. Integrating with Your Actual Project</strong></h3>
<p>You have two main approaches to bring these meta-tools into your real project:</p>
<ol>
    <li><strong>Submodule Approach</strong>
        <pre class="code-block"><code>git submodule add https://github.com/specifiedcodes/ContextforAIcoder.git context</code></pre>
        Now you have a <code>context/</code> folder with all scripts. You can rename or move the <code>.template</code> files and start using them.
    </li>
    <li><strong>Manual Copy</strong><br />
        Simply copy <code>context/</code> into your project.<br />
        You lose the direct link to updates in <code>ContextforAIcoder</code>, but it may be simpler if you prefer a one-off integration.
    </li>
</ol>

<hr />

<h3><strong>C. Setting Up <code>.cursorrules</code> and <code>PROJECT_CONTEXT.json</code></strong></h3>
<ol>
    <li>Rename <code>cursorrules.template.json</code> → <code>.cursorrules</code> (or <code>cursorrules.json</code>) in your project’s root.</li>
    <li>Fill <code>PROJECT_CONTEXT.template.json</code> → <code>PROJECT_CONTEXT.json</code> with real details about your project:
<pre class="code-block"><code>{
  "project_name": "My Cool Finance App",
  "description": "A containerized Node.js + Next.js finance project",
  "features": [
    "User auth",
    "Transaction management"
  ]
  ...
}
</code></pre>
    </li>
    <li>Edit the contents to reflect your code style. For example, if you prefer JSDoc over XML doc comments, change the rules in <code>.cursorrules</code>.</li>
</ol>

<hr />

<h3><strong>D. Referencing <code>.cursorrules</code> in Cursor or Other AI Tools</strong></h3>
<p>
Cursor (or any AI IDE extension) doesn’t automatically parse <code>.cursorrules</code> unless specifically supported.<br />
At a minimum, open the <code>.cursorrules</code> file in your editor and tell the AI, “Please follow the rules in <code>.cursorrules</code> for doc/comments.”<br />
Alternatively, you can include <code>.cursorrules</code> content in your system or user prompt if you’re using ChatGPT, Bing Chat, or a local LLM environment.
</p>

<hr />

<h3><strong>E. Using the Vector Database</strong></h3>
<p><strong>Semantic Search or Q&amp;A about your code:</strong></p>
<div class="code-block">
<pre><code>from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

db = Chroma(collection_name="finance-project", persist_directory=".chroma")
query = "Where is the transaction logic handled?"
results = db.similarity_search(query)
print(results)
</code></pre>
</div>
<p>
This returns the top matching docs/snippets. You can pass those snippets to your AI to provide deeper context.<br />
<strong>Advanced:</strong> Build a LangChain “retrieval-augmented” system that automatically injects relevant code docs into your AI prompts. This can be done by creating a pipeline or chain in Python that uses the Chroma store, queries your docs, and calls an LLM with the retrieved context.
</p>

<hr />

<h2><strong>Advanced Tips &amp; Customizations</strong></h2>
<ul>
    <li><strong>Chunking Large Files</strong><br />
    If you have large source files or docs, you might want to chunk them. Within <code>update_embeddings.py</code>, consider splitting content into segments before embedding.</li>
    <li><strong>Auth/Keys</strong><br />
    If you’re using <code>OpenAIEmbeddings</code>, you need your <code>OPENAI_API_KEY</code> in the environment, for example:
    <pre class="code-block"><code>export OPENAI_API_KEY="sk-..."
</code></pre>
    </li>
    <li><strong>Alternative Embeddings</strong><br />
    If you prefer offline embeddings, install <code>sentence-transformers</code> or <code>HuggingFaceEmbeddings</code> instead of <code>OpenAIEmbeddings</code>.</li>
    <li><strong>Performance</strong><br />
    Watchdog-based watchers can be resource-intensive on large projects. Use the Git hook approach for a more lightweight option.</li>
    <li><strong>Git Hooks</strong><br />
    Example: a <code>pre-commit</code> hook that calls <code>update_embeddings.py</code> for staged files only, ensuring all changed code is re-embedded before commits.</li>
</ul>

<hr />

<h2><strong>Recommended Workflow</strong></h2>
<ol>
    <li>Create/Copy <code>.cursorrules</code> and <code>PROJECT_CONTEXT.json</code> into each project.</li>
    <li>Run <code>python watch_changes.py</code> to keep embeddings fresh automatically.</li>
    <li>Use your AI tool (Cursor, ChatGPT, local LLM) to reference <code>.cursorrules</code> for consistent doc/comment style.</li>
    <li>(Optional) Build or run a query script to do semantic searches over your code.</li>
    <li>Iterate on your <code>.cursorrules</code> and <code>PROJECT_CONTEXT.json</code> as your style rules or project features evolve.</li>
</ol>

<hr />

</body>
