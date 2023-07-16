Module & it's Elements Dependencies
===================================

.. toctree:: 
    :maxdepth: 3
    :caption: Table of Contents:

Coupling
--------
Coupling refers to the degree of interdependence between different modules or components in a software system. It measures how closely and extensively one module relies on another module. High coupling means modules are tightly interconnected, making changes in one module likely to impact other modules. Low coupling indicates that modules are more independent, allowing changes to be localized and reducing the ripple effects of modifications.

Types of Coupling
~~~~~~~~~~~~~~~~~
Temporal Coupling
""""""""""""""""""
.. note::
    | **Temporal:** Relating to Time
    | **Spatial:** Relating to the position, area, and size of things

Temporal Coupling occurs when there's an implicit relationship between two, or more, members of a class requiring clients to invoke one member before the other. This tightly couples the members in the temporal dimension.

Example
''''''''
This example describes a more abstract code smell, exhibited by the Smell class. The public API looks like this:

.. code-block:: java
   :linenos:

   public class Smell
   {
      public void Initialize(string name)
    
      public string Spread()
   }

Semantically the name of the Initialize method is obviously a clue, but on a structural level this API gives us no indication of temporal coupling. Thus, code like this compiles, but throws an exception at run-time:

.. code-block:: java
   :linenos:

   var s = new Smell();
   var n = s.Spread();

It turns out that the Spread method throws an InvalidOperationException because the Smell has not been initialized with a name. The problem with the Smell class is that it doesn't properly protect its invariants. In other words, encapsulation is broken.

To fix the issue the Initialize method must be invoked before the Spread method:

.. code-block:: java
   :linenos:

   var sut = new Smell();
   sut.Initialize("Sulphur");
   var n = sut.Spread();

Solution
''''''''''
Encapsulation requires that the class can never be in an inconsistent state. Since the name of the smell is required, a guarantee that it is always available must be built into the class. If no good default value is available, the name must be requested via the constructor:

.. code-block:: java
   :linenos:
   
   public class Fragrance : IFragrance
   {
      private readonly string name;
   
      public Fragrance(string name)
      {
         if (name == null)
         {
               throw new ArgumentNullException("name");
         }
   
         this.name = name;
      }
   
      public string Spread()
      {
         return this.name;
      }
   }

Cohesion
--------


References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. https://blog.ploeh.dk/2011/05/24/DesignSmellTemporalCoupling/