Images
======

To add an image, use one of the following directives.



.. image:: image.png
  :width: 150 pt
  :align: center
  
Or if caption/ legend is needed.

.. figure:: figure.png
   :width: 150 pt
   :align: center
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph and the following
   table:

   +-----------------------+-----------------------+
   | Symbol                | Meaning               |
   +=======================+=======================+
   | .. image:: tent.png   | Campground            |
   |    :width: 20 pt      |                       |
   +-----------------------+-----------------------+
   | .. image:: waves.png  | Lake                  |
   |    :width: 20 pt      |                       |
   +-----------------------+-----------------------+
   | .. image:: peak.png   | Mountain              |
   |    :width: 20 pt      |                       |
   +-----------------------+-----------------------+
