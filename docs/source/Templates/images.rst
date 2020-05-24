Images
======

To add an image, use one of the following directives.



.. image:: image.png
  :width: 150 px
  :height: 150 px
  :align: center
  
Or if caption/ legend is needed.

.. figure:: figure.png
   :width: 150 px
   :height: 150 px
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
   |    :width: 50 px      |                       |
   |    :height: 50 px     |                       |
   +-----------------------+-----------------------+
   | .. image:: waves.png  | Lake                  |
   |    :width: 50 px      |                       |
   |    :height: 50 px     |                       |
   +-----------------------+-----------------------+
   | .. image:: peak.png   | Mountain              |
   |    :width: 50 px      |                       |
   |    :height: 50 px     |                       |
   +-----------------------+-----------------------+
