Images
======

To add an image, use one of the following directives.



.. image:: image.png
  :width: 150 px
  :height: 150 px
  :scale: 50 %
  :align: center
  
Or if caption/ legend is needed.

.. figure:: figure.png
   :scale: 50 %
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
   |    :scale: 10 %       |                       |
   +-----------------------+-----------------------+
   | .. image:: waves.png  | Lake                  |
   |    :scale: 10 %       |                       |
   +-----------------------+-----------------------+
   | .. image:: peak.png   | Mountain              |
   |    :scale: 10 %       |                       |
   +-----------------------+-----------------------+
