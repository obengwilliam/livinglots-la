from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import AsTag
from django import template

from ladata.buildings.models import Building


register = template.Library()


class GetSpecialCategories(AsTag):
    options = Options(
        'for',
        Argument('lot', resolve=True, required=True),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context, lot):
        categories = []
        for l in lot.lots:
            if l.parcel.sidelot_set.count() > 0:
                categories.append('Side Yard')
        return categories


class GetVacantReasons(AsTag):
    options = Options(
        'for',
        Argument('lot', resolve=True, required=True),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context, lot):
        reasons = []
        building_outlines_url = 'http://egis3.lacounty.gov/dataportal/2011/04/28/countywide-building-outlines/'
        local_roll_url = 'http://assessor.lacounty.gov/extranet/outsidesales/gisdata.aspx'

        for l in lot.lots:
            if l.friendly_owner:
                reasons.append('The owner opted to add it to our map')
            if l.parcel.is_coded_vacant:
                reasons.append("""
                    Its use code is vacant according to the
                    <a href="%s" target="_blank">LA County Assessor</a>
                """ % local_roll_url)
            if l.parcel.sidelot_set.count() > 0:
                reasons.append("It is in the city's sidelot data")
            if l.parcel.transmissionline_set.count() > 0:
                reasons.append('It is under a transmission line')
            if l.parcel.weedabatement_set.count() > 0:
                reasons.append('It is marked for weed abatement')
            if not Building.objects.filter(geom__overlaps=lot.polygon).exists():
                reasons.append("""
                    There are no buildings on it according to the
                    <a target="_blank" href="%s">county building outlines</a>
                """ % building_outlines_url)

            improvement_value = l.parcel.local_roll.improvement_value
            if not improvement_value or improvement_value is 0:
                reasons.append("""
                    It has no improvement value according to the
                    <a href="%s" target="_blank">LA County Assessor</a>
                """ % local_roll_url)
        return list(set(reasons))


register.tag(GetSpecialCategories)
register.tag(GetVacantReasons)
