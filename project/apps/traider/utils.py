from django.utils.safestring import mark_safe

# for image resize
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO


class QueryString(object):
    """
    QueryString (GET query string tool)
    Usage:
        no__name1__name2    - exclude variables by name in "no" section
        only__name1__name2  - only variables with name in "only" section
        as__format[left]    - return querydict in format (must be at the end)
                              if left, also add &(?) at the end of querystring

    Format available values:
        ┌─────────┬───────────┬───────────┬───────────┬───────────────┐
        │         │ query,    │ query,    │ no query, │ no query,     │
        │         │ left      │ no left   │ left      │ no left       │
        ├─────────┼───────────┼───────────┼───────────┼───────────────┤
        │ full    │ "?a=a&"   │ "?a=a"    │ "?"       │ ""            │
        │ part    │ "&a=a&"   │ "&a=a"    │ "&"       │ ""            │
        │ self    │ "a=a&"    │ "a=a"     │ ""        │ ""            │
        ├─────────┼───────────┴───────────┴───────────┴───────────────┤
        │ dict    │ return query as is (QueryDict)                    │
        └─────────┴───────────────────────────────────────────────────┘
    Examples:
        http://example.com/?a=a&b=b&c=c
        q = QueryString(request)
        q.as__dict              # copy of QueryDict from request
        q.no__a__b__as__self    # c=c
        q.no__a__b__as__full    # ?c=c
        q.no__c__as__partleft   # &a=a&b=b&
        q.only__c__as__partleft # &c=c&
    """

    querydict = None

    formats = ('part', 'full', 'self', 'dict',)
    filters = ('no', 'only',)
    first_letter = {'full': '?', 'part': '&', 'self': '',}

    def __init__(self, request):
        self.querydict = request.GET.copy()

    def __getattr__(self, name):
        data = name.rsplit('as__')
        keys = data[0].strip('__').split('__')[:]
        out = data[1] if data.__len__() > 1 else 'full'
        out = {'format': out[:4] if out[:4] in self.formats else 'full',
               'left': out.endswith('left'),}
        query = self.querydict.copy()

        # morph query by filter
        if keys.__len__() > 1 and keys[0] in self.filters:
            action, keys, realkeys = keys[0], keys[1:], list(query.keys())
            if 'no' == action:
                [query.pop(i, None) for i in keys]
            else:  # only
                [query.pop(i, None) for i in realkeys if i not in keys]

        # output format
        if out['format'] != 'dict':
            first = self.first_letter[out['format']]
            query = query.urlencode()
            query = mark_safe(''.join((
                first if query else '', query,  # first letter and querystring
                ('&' if query else first) if out['left'] else '',  # last letter
            )))

        return query


image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    # Open the image using Pillow
    img = Image.open(image)
    # check if either the width or height is greater than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(image.file.name).name.split(".")[-1]
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_filename, file_object)

def calculate_avg_percent(any_model):
        avg_loss_perc = '{:.3f}'.format(
            sum([i.result_percent for i in lost_traids]) \
            / lost_traids.count()
        )
