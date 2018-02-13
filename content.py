# coding=UTF-8
CONTENT = '''
<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <title>Ideas page for GSoC 2018 | Python Hydra</title>
  <style media="screen">
    a.anchor {
      display: block;
      position: relative;
      top: -80px;
      visibility: hidden;
    }
  </style>
</head>

<body>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top align-items-center p-3 px-md-4 bg-white border-bottom box-shadow">
    <h5 class="my-0 mr-md-auto font-weight-normal"> <img src="https://www.hydra-cg.com/img/logo.png" class= "pr-2"width="55px" alt="Hydra CG logo"><a href="https://hydra-cg.com/" style=" text-decoration: none !important; color:black">Python HYDRA</a> </h5>
    <div class="my-2 my-md-0 mr-md-3">
      <a class="p-2 text-dark d-none d-md-inline d-xl-inline" href="#inspiration">Our Inspiration</a>
      <a class="p-2 text-dark  d-none d-md-inline d-xl-inline" href="#hydrus">About Hydrus</a>
      <a class="p-2 text-dark  d-none d-md-inline d-xl-inline" href="#getting-started">Getting Started</a>
    </div>
    <a class="btn btn-outline-primary d-none d-sm-inline d-md-inline d-xl-inline" href="#ideas">Project Ideas</a>
  </nav>



  <div class="container mt-5 pt-5">

    <div class="banner text-center">
      <h1>Hydra W3C Community</h1>
      <h2>Ideas Page for Google Summer of Code 2018</h2>
    </div>
    <div class="px-1 py-1 pt-md-5 mx-auto">
      <a class="anchor" id="inspiration"></a>
      <h1 class="display-4">Our Inspiration</h1>
      <p class="lead font-weight-normal">
        Building Web APIs seems still more an art than a science. How can we build APIs such that generic clients can easily use them? And how do we build those clients? Current APIs heavily rely on out-of-band information such as human-readable documentation
        and API-specific SDKs. However, this only allows for very simple and brittle clients that are hardcoded against specific APIs. Hydra, in contrast, is a set of technologies that allow to design APIs in a different manner, in a way that enables
        smarter clients.
        <br>You can read more <a href="https://www.hydra-cg.com/">here</a>
      </p>
    </div>
    <hr>
    <div class="px-1 py-1 pb-md-4 mx-auto">
      <a class="anchor" id="hydrus"></a>
      <h1 class="display-4">About Hydrus</h1>
      <p class="lead  font-weight-normal">
        Hydrus is a set of Python based tools for easier and efficient creation of Hypermedia driven REST-APIs. Hydrus utilises the power of <a href="https://en.wikipedia.org/wiki/Linked_data">Linked Data</a> to create a powerful REST APIs to serve data.
        Hydrus uses the <a href="https://www.hydra-cg.com/">Hydra(W3C)</a> standard for creation and documentation of it's APIs.
      </p>
      <h3>Features</h3>
      <ul class="lead  font-weight-normal">
        <li>A client that can understand Hydra vocabulary and interacts with a Hydra supporting server to basic <a href="https://en.wikipedia.org/wiki/Create,_read,_update_and_delete">CRUD</a> operations on data.</li>
        <li>A generic server that can serve required data and metadata(in the form of API documentation) to a client over HTTP.</li>
        <li>A middleware that allows users to use the client to interact with the server using Natural Language which is processed machine consumable language. (under developement)</li>
      </ul>
    </div>
    <hr>
    <div class="px-1 py-1 pb-md-4 mx-auto">
      <a class="anchor" id="getting-started"></a>

      <h1 class="display-4">How do I get started ?</h1>
      <p class="lead  font-weight-normal">
        Getting started is pretty easy. Head over to our <a href="https://www.hydra-cg.com/">community page</a>. There are a lot of demos, presentations, and talks to get you up to speed. Then head over to the <a href="https://github.com/HTTP-APIs/hydrus">Hydrus repo</a>        and clone it. Play with it a little, try to understand how the current implementation works, try to fix some bugs or report any issues you can find <a href="https://github.com/HTTP-APIs/hydrus/issues">here</a>.
        <br> Lastly, don't hesitate to reach out in the <a href="https://gitter.im/HTTP-APIs/Lobby" target="_blank">Gitter channel</a> if you have any question, we are very friendly people and we'll be more than happy to help you out.
      </p>
      <p class="lead  font-weight-normal">As a general entrypoint to understand the repositories, there is the <a href="https://github.com/HTTP-APIs/hydrus/wiki">Hydrus Wiki</a> and related links. Having a clear insight of <a href="https://goo.gl/TCdYG3">Resource Description Framework</a>        is quite necessary, Mentors will give full support to catch up with it.</p>
      <br>
      <div class="faq lead font-weight-normal">
        <h3>FAQ</h3>
        <details>
          <summary>What is Google Summer of Code?</summary>
          <hr>
          <p>Google Summer of Code (GSoC) is a global program that matches students up with open source, free software and technology-related organizations to write code and get paid to do it! The organizations provide mentors who act as guides through the
            entire process, from learning about the community to contributing code. The idea is to get students involved in and familiar with the open source community and help them to put their summer break to good use.</p>
          <p>You can read Google <a href="https://developers.google.com/open-source/gsoc/resources/guide#student_manual">Student Manual</a> for more info.</p>
          <hr>
        </details>
        <details>
          <summary>How to write a proposal?</summary>
          <hr>
          <p>Writing a good proposal can be a really challenging task. We have curated a list of helpful resources to help you get started.</p>
          <ul>
            <li>
              <a href="http://people.csail.mit.edu/baghdadi/TXT_blog/5_advices_to_get_your_proposal_accepted.lyx.html">5 Tips to get your Google Summer of Code proposal accepted</a>
            </li>
            <li>
              <a href="https://www.quora.com/How-to-write-a-good-GSoC-proposal">How to write a good GSoC proposal (Quora) ?</a>
            </li>
            <li>
              <a href="http://teom.org/blog/kde/how-to-write-a-kick-ass-proposal-for-google-summer-of-code/">How to write a kick-ass proposal for Google Summer of Code</a>
            </li>

          </ul>
          <hr>
        </details>

        <details>
          <summary>Proposal template</summary>
          <hr>

          <p><a href="https://docs.google.com/document/d/1qPR02o6jY4uFBdCf3S0ous4LG32YCe6ZJuDGojXH2JY/edit">Here</a>'s a proposal template for you to get started.</p>

          <hr>
        </details>
      </div>
      <br>

      <h3>Communication Channels</h3>
      <ul class="lead  font-weight-normal">
        <li><a href="https://gitter.im/HTTP-APIs/Lobby">Gitter</a> </li>
        <li><a href="https://www.w3.org/community/hydra/">W3C Group</a> </li>
        <li>
          <span>Email</span>
          <ul>
            <li><a href="mailto:tunedconsulting@gmail.com">Lorenzo Moriondo</a> </li>
            <li><a href="mailto:xadahiya@gmail.com">Akshay Dahiya</a> </li>
            <li><a href="mailto:chrisandrew119@gmail.com">Chris Andrew</a> </li>
            <li><a href="mailto:kristian.koci@gmail.com">Kristian Koci</a> </li>
            <li><a href="mailto:damrgrass@gmail.com">Matteo Franchi</a> </li>
          </ul>
        </li>
      </ul>
    </div>
    <hr>
    <div class="px-1 py-1 pb-md-4 mx-auto">
      <a class="anchor" id="ideas"></a>

      <h1 class="display-4">Project Ideas</h1>
      <p class="lead font-weight-normal">The ideas are arranged in increasing order of difficulty. Please feel free to combine several ideas into your proposal.</p>
      <br>
      <h2>Ideas Related to Hydrus</h2>

      <hr>
      <div class="idea">

        <h3>1. Design a Command line interface for Hydrus</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Although Hydrus is primarily a Python-based library right now, most Hydra users may not be familiar with Python to set up servers. It would be great if we could have a CLI for Hydrus where users would just need to pass parameters to set up a server
          and get it up and running. Also, the current process of server setup is long and needs a lot of prerequisite knowledge to be able to set up. This process needs to be abstracted to make it simpler, and more powerful for a user to have more control
          over the server. Maybe something similar to Python’s SimpleHTTPServer.</p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Flask</li>
          <li>Command Line</li>
          <li>Basic knowledge of Semantic Web and Graph Databases</li>
          <li>Ability to learn new technologies quickly</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Easy to Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydrus Repo</a> </li>
          <li><a href="https://github.com/HTTP-APIs/hydrus/wiki/">Hydrus Wiki</a> </li>
          <li><a href="https://gsocchrizandr.wordpress.com/the-book-of-hydrus/">The Book of Hydrus</a> </li>
          <li><a href="https://www.hydra-cg.com/spec/latest/core/">Hydra Draft</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>


      <div class="idea">

        <h3>2. Better API Querying</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Right now, we only have no mechanism for searching an instance of a class in the Hydra API. Most APIs implement a search feature where the data is queried using a defined syntax. This is more of an issue with Hydra itself as the mechanism for
          search is not defined in Hydra yet. It would be great if we can have some advance querying functionality like they have in graph databases.</p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Flask</li>
          <li>Python</li>
          <li>Sqlalchemy</li>
          <li>PostgreSQL</li>
          <li>Command Line</li>
          <li>Basic knowledge of Semantic Web and Graph Databases</li>
          <li>Basic knowledge of graph querying languages</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus/wiki/Design#dbdesign">Hydrus Database Design</a> </li>
          <li><a href="https://developer.ibm.com/dwblog/2017/overview-graph-database-query-languages/">Graph querying languages overview</a> </li>
          <li><a href="https://gsocchrizandr.wordpress.com/the-book-of-hydrus/">The Book of Hydrus</a> </li>
          <li><a href="https://www.hydra-cg.com/spec/latest/core/">Hydra Draft</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

      <div class="idea">

        <h3>3. Python Client Implementation</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Implement a generic Hydra client that can reference an API Documentation and allow users to interact with an API using objects, rather than URIs/paths. The HydraConsole is a good reference client to use, and we could extend functionality and implement
          a Python version of it. More ideas are welcome on this.</p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Strong Knowledge of Graphs</li>
          <li>At least basic knowledge of RDF</li>
          <li>JSON and JSON-LD</li>
          <li>Python</li>
          <li>Command Line</li>
          <li>Basic knowledge of Semantic Web</li>
          <li>Ability to learn new technologies quickly</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate to Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/pchampin/hydra-py">Current implementation by @pchampin</a> </li>
          <li><a href="https://www.w3.org/RDF/">RDF overview</a> </li>
          <li><a href="https://en.wikipedia.org/wiki/JSON-LD">JSON-LD wiki</a> </li>
          <li><a href="https://gsocchrizandr.wordpress.com/the-book-of-hydrus/">The Book of Hydrus</a> </li>
          <li><a href="https://www.hydra-cg.com/spec/latest/core/">Hydra Draft</a> </li>
          <li><a href="https://www.markus-lanthaler.com/hydra/console/">Hydra Console</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>


      <div class="idea">

        <h3>4. Switch to Python Falcon server</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Falcon is a minimalist WSGI library for building speedy web APIs and app backends. When it comes to building HTTP APIs, other frameworks weigh you down with tons of dependencies and unnecessary abstractions. Falcon cuts to the chase with a clean
          design that embraces HTTP and the REST architectural style. Hydrus is currently implemented using Flask, we're thinking about switching to Falcon.</p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Sqlalchemy</li>
          <li>Falcon Web Framework</li>
          <li>Command Line</li>
          <li>Basic knowledge of Semantic Web</li>
          <li>Ability to learn new technologies quickly</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://falcon.readthedocs.io/en/latest/">Falcon Docs</a> </li>
          <li><a href="https://falcon.readthedocs.io/en/latest/user/tutorial.html#creating-resources">Creating resource with Falcon</a> </li>
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydus Github Repo</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

      <div class="idea">

        <h3>5. More User defined Controls for the server</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">There is no way right now to actually change the way the client accesses the server set up by Hydrus. Although there is some support for Authentication/Authorization, the actual implementations are very basic and do not offer much security features.
          There is also no way to control server access or limit/modify user privilege. There may be APIs that provide different levels of access to different users. There are also bottlenecks in place in REST APIs that limit the number of requests each
          user can make, such control is not given to users. There needs to be a way to add additional controls to the server, that can be built on top of the original Hydrus app.</p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Flask</li>
          <li>Strong knowledge of Authentication and Authorization in various APIs</li>
          <li>Basic knowledge of Semantic Web</li>
          <li>Ability to learn new technologies quickly</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydus Github Repo</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>


      <div class="idea">

        <h3>6. Django-rest-hydra</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Hydrus is developed in Flask because the applications we had in mind were mostly related to IoT and sensors, so it was supposed to be lightweight and functional. But if we may want to look for more traditional applications and the wider public,
          we may like to have a Django library ( <a href="http://hirokiky.org/tech/create_django_library.html">http://hirokiky.org/tech/create_django_library.html</a> ) that does have the same features as hydrus but works with Django.</p>
        <p class="lead font-weight-normal">As Django has already a well-established REST library (Django-rest) it would be probably useful to extend it and create something like Django-rest-hydra, a library that let Django developers deploy hydra server in Django as now hydrus does with
          flask (starting from an RDF vocabulary or an OpenAPI definition).</p>
        <p class="lead font-weight-normal">
          <b>Note: </b><a href="https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html
">How to create a Django middelware</a>
        </p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Django</li>
          <li>Django rest</li>
          <li>Basic knowledge of Semantic Web</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="http://hirokiky.org/tech/create_django_library.html">Creating a Django Library</a> </li>
          <li><a href="https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html">How to create a Django middleware.</a> </li>
          <li><a href="http://www.django-rest-framework.org/">Django rest framework</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>



      <div class="idea">

        <h3>7. Support Redis as Graph database</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Graph based data is everywhere now days, Facebook, Google, Twitter and Pinterest are only a few who've realize the power behind relationship data and are utilizing it to the fullest, as a direct result we see a rise both in interest and variety
          of graph data solutions.</p>
        <p class="lead font-weight-normal">RedisGraph is a graph database developed from scratch on top of Redis, using the new Redis Modules API to extend Redis with new commands and capabilities. Its main features include: - Simple, fast indexing and querying - Data stored in RAM, using
          memory-efficient custom data structures - On disk persistence - Tabular result sets - Simple and popular graph query language (Cypher) - Data Filtering, Aggregation and ordering.</p>
        <p class="lead font-weight-normal">
          Currently Hydrus uses a relational database model to store graph data. It would be interesting to switch to a graph databasee like Redis. We need to implement a multi-layered hexastore to store graph data. This will also help in the implementation of
          <b>Idea #2 - Better API querying</b>.
        </p>
        <h4>Skills Required</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Flask</li>
          <li>Basic knowledge of graph databases</li>
          <li>Ability to learn new technologies quickly</li>
          <li>Basic knowledge of Semantic Web</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="http://redisgraph.io/design/">Redis Graph : A graph database module for Redis</a> </li>
          <li><a href="https://redis.io/topics/indexes#representing-and-querying-graphs-using-an-hexastore">Paper on representing and querying graphs using an hexastore.</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>


      <h2>Ideas Related to Demos using Hydrus</h2>
      <hr>
      <div class="idea">

        <h3>1. Demonstration with Dynamic API paths</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">If we can create an API whose structure(paths to different kinds of data) is constantly changing only the vocab path stays same. Then we can use a Hydra client to discover the required paths for various kinds of data. This can be a great way to
          demonstrate the capabilities and use cases of HTTP-APIs and Hydra in general. We can have a UI showing the API structure in real-time and allow users to POST/GET/PUT/DELETE any type of data. We can also show how the client and API server interact
          with each other ( We had a lot of requests going on in the drone demo and it was very difficult to understand how things are working in the background.) For example: Suppose we have a Student class with basic properties like Name, Id, Class
          etc. Then the user can request for data say "Students with Id = 1*" without knowing anything about the API structure as it's dynamic. We can also demonstrate advanced querying features with this.</p>
        <h4>Required Skills</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Linux</li>
          <li>Server Management</li>
          <li>At least basic knowledge of DevOps</li>
          <li>HTML, CSS, JS</li>
          <li>Knowledge of any Javascript framework is a plus ( React Js or Vue Js)</li>
          <li>Basic Knowledge of Semantic Web</li>
          <li>High problem-solving abilities</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate to Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydus Github Repo</a> </li>
          <li><a href="https://github.com/HTTP-APIs/hydra-flock-demo">A sample drone simulation</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

      <div class="idea">

        <h3>2. Satellite and Subsystems Demo</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">We may finally end up implementing the astronomy/satellites vocabulary as thought in the beginning. We need a way to demonstrate how Hydra can be utilized by Satellites to communicate with each other and get information about each of their subsystems
          and statuses. The OWL Vocabulary for Subsystems is given <a href="https://github.com/chronos-pramantha/RDFvocab">here</a>. We need to create a Hydra Spec for a demo system that will use these ontologies for a demo.</p>
        <h4>Required Skills</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Linux</li>
          <li>Server Management</li>
          <li>At least basic knowledge of DevOps</li>
          <li>HTML, CSS, JS</li>
          <li>Knowledge of any Javascript framework is a plus ( React Js or Vue Js)</li>
          <li>Basic Knowledge of Semantic Web</li>
          <li>High problem-solving abilities</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate to Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydus Github Repo</a> </li>
          <li><a href="https://github.com/HTTP-APIs/hydra-flock-demo">A sample drone simulation</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>


      <div class="idea">

        <h3>3. Rail Management System</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">We can have a cool demo about railway management where trains are routed based on available tracks and are assigned platforms and routes based on live information taken from several trains. This could be a good demo to showcase how Hydra can be
          used as a generic language since not all railway stations would use the same API to convey information to trains. We could have multiple Hydra based APIs running on railway stations and trains and all of them communicating with each other using
          Hydra and a common Vocabulary. We still need to find a vocabulary for this, or we could also create one.</p>
        <h4>Required Skills</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Linux</li>
          <li>Server Management</li>
          <li>At least basic knowledge of DevOps</li>
          <li>HTML, CSS, JS</li>
          <li>Knowledge of any Javascript framework is a plus ( React Js or Vue Js)</li>
          <li>Basic Knowledge of Semantic Web</li>
          <li>High problem-solving abilities</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Intermediate to Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://github.com/HTTP-APIs/hydrus">Hydus Github Repo</a> </li>
          <li><a href="https://github.com/HTTP-APIs/hydra-flock-demo">A sample drone simulation</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

      <h2>Other Ideas</h2>
      <hr>


      <div class="idea">

        <h3>1. Create a QGIS plugin</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Create a QGIS plugin that works with hydrus. QGIS is an opensource geospatial client, geospatial clients are used to load maps in different formats (images, rasters, vectors). QGIS can work as an HTTP client to fetch data from special Web services
          called OGC Web Standards (WMS, WMTS, WFS). Plugin for QGIS can be developed in Python, a QGIS-HYDRA plugin may be able to query geospatial data stored in hydrus using the HYDRA vocabulary. The same functionality could be accomplished with a
          MapBox or LeafLet client app that uses a python-hydra client as middleware and hydrus as a backend.</p>
        <h4>Required Skills</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Basic Knowledge of Semantic Web</li>
          <li>Good Knowledge of GIS software ecosystem</li>
          <li>High problem-solving abilities</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li><a href="https://qgis.org/en/site/">QGIS Homepage</a> </li>
          <li><a href="https://github.com/qgis">QGIS Github Repo</a> </li>
          <li><a href="https://en.wikipedia.org/wiki/Open_Geospatial_Consortium#Standards">OpenGeoSpatial Consortium Web standards</a> </li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

      <div class="idea">

        <h3>2. Keep Hydrus up-to-date with Hydra Specs</h3>
        <br>
        <h4>Description</h4>
        <p class="lead font-weight-normal">Hydra <a href="https://github.com/HydraCG/Specifications/issues" target="_blank">
            Draft Specs</a> are evolving and Hydrus needs to follow the most recent updates in the Specs. Code has to be amended to implement new features.</p>
        <h4>Required Skills</h4>
        <ul class="lead font-weight-normal">
          <li>Python</li>
          <li>Git</li>
          <li>Good Knowledge of Semantic Web and REST paradigm</li>
          <li>High problem-solving abilities</li>
          <li>Ability to write test suites</li>
        </ul>

        <h4>Difficulty Level - Hard</h4>
        <h4>Related Links</h4>
        <ul class="lead font-weight-normal">
          <li>Hydra <a href="https://github.com/HydraCG/Specifications/issues" target="_blank">Draft Specs</a></li>
        </ul>
        <h4>Potential Mentors</h4>
        <p class="lead font-weight-normal">
          <a href="https://www.linkedin.com/in/lorenzomoriondo/">Lorenzo Moriondo</a>,
          <a href="https://www.linkedin.com/in/xadahiya/">Akshay Dahiya</a>,
          <a href="https://www.linkedin.com/in/chrizandr/">Chris Andrew</a>,
          <a href="https://www.linkedin.com/in/kristian-koci-1304a025/">Kristian Koci</a>,
          <a href="https://www.linkedin.com/in/matteofranchi">Matteo Franchi</a>
        </p>
        <hr>
      </div>

    </div>

    <div id="disqus_thread"></div>
    <script>
      (function() { // DON'T EDIT BELOW THIS LINE
        var d = document,
          s = d.createElement('script');
        s.src = 'https://hydra-gsoc.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
      })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  </div>
  </div>

  <footer class="footer text-center pb-2">
    <div class="container">
      <span class="">Made with <img src="https://img00.deviantart.net/9855/i/2016/130/b/7/undertale___pixel_heart_thingy_by_aspalax-da1zkgz.png" alt="love" width="20px"> by Hydra Community Group.</span>
    </div>
  </footer>

</body>

</html>
'''
