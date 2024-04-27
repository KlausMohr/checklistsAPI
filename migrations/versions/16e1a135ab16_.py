"""empty message

Revision ID: 16e1a135ab16
Revises: 
Create Date: 2024-04-25 19:44:06.794768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16e1a135ab16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_exterior', schema=None) as batch_op:
        batch_op.drop_constraint('tb_exterior_doors_hood_tailgate_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_exterior_grille_trim_roof_rack_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_exterior_glass_outside_mirrors_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_exterior_exterior_lights_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_exterior_body_panels_bumper_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tb_grille_trim_roof_rack', ['grille_trim_roof_rack_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_exterior_lights', ['exterior_lights_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_body_bumper', ['body_panels_bumper_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_glass_outside_mirrors', ['glass_outside_mirrors_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_doors_hood_tailgate', ['doors_hood_tailgate_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')

    with op.batch_alter_table('tb_interior', schema=None) as batch_op:
        batch_op.drop_constraint('tb_interior_heat_ac_defog_defrost_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_carpet_trims_mats_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_audio_alarm_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_interior_amenities_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_seats_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_airbag_safety_belts_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_luggage_compartment_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_windows_doors_locks_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_interior_sunroof_convertible_top_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tb_carpet_trim_mats', ['carpet_trims_mats_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_audio_alarm', ['audio_alarm_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_seats', ['seats_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_luggage_compartment', ['luggage_compartment_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_airbag_safety_belts', ['airbag_safety_belts_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_heat_ac_defog_defrost', ['heat_ac_defog_defrost_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_windows_doors_locks', ['windows_doors_locks_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_interior_amenities', ['interior_amenities_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_sunroof_convertible_top', ['sunroof_convertible_top_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')

    with op.batch_alter_table('tb_ownership', schema=None) as batch_op:
        batch_op.drop_constraint('tb_ownership_owner_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_ownership_vehicle_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tb_owner', ['owner_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_vehicle', ['vehicle_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')

    with op.batch_alter_table('tb_underbody', schema=None) as batch_op:
        batch_op.drop_constraint('tb_underbody_tires_wheels_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underbody_exhaust_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underbody_trans_diff_transfer_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underbody_brake_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underbody_frame_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tb_brake', ['brake_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_tires_wheels', ['tires_wheels_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_frame', ['frame_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_exhaust', ['exhaust_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_transmission_differential', ['trans_diff_transfer_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')

    with op.batch_alter_table('tb_underhood', schema=None) as batch_op:
        batch_op.drop_constraint('tb_underhood_cooling_system_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underhood_fluids_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underhood_engine_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underhood_engine_electrical_system_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('tb_underhood_fuel_system_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'tb_engine', ['engine_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_fuel_system', ['fuel_system_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_engine_electrical_system', ['engine_electrical_system_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_cooling_system', ['cooling_system_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'tb_fluids', ['fluids_id'], ['id'], referent_schema='checklist_app', ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_underhood', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tb_underhood_fuel_system_id_fkey', 'tb_fuel_system', ['fuel_system_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underhood_engine_electrical_system_id_fkey', 'tb_engine_electrical_system', ['engine_electrical_system_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underhood_engine_id_fkey', 'tb_engine', ['engine_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underhood_fluids_id_fkey', 'tb_fluids', ['fluids_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underhood_cooling_system_id_fkey', 'tb_cooling_system', ['cooling_system_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('tb_underbody', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tb_underbody_frame_id_fkey', 'tb_frame', ['frame_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underbody_brake_id_fkey', 'tb_brake', ['brake_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underbody_trans_diff_transfer_id_fkey', 'tb_transmission_differential', ['trans_diff_transfer_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underbody_exhaust_id_fkey', 'tb_exhaust', ['exhaust_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_underbody_tires_wheels_id_fkey', 'tb_tires_wheels', ['tires_wheels_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('tb_ownership', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tb_ownership_vehicle_id_fkey', 'tb_vehicle', ['vehicle_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_ownership_owner_id_fkey', 'tb_owner', ['owner_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('tb_interior', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tb_interior_sunroof_convertible_top_id_fkey', 'tb_sunroof_convertible_top', ['sunroof_convertible_top_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_windows_doors_locks_id_fkey', 'tb_windows_doors_locks', ['windows_doors_locks_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_luggage_compartment_id_fkey', 'tb_luggage_compartment', ['luggage_compartment_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_airbag_safety_belts_id_fkey', 'tb_airbag_safety_belts', ['airbag_safety_belts_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_seats_id_fkey', 'tb_seats', ['seats_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_interior_amenities_id_fkey', 'tb_interior_amenities', ['interior_amenities_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_audio_alarm_id_fkey', 'tb_audio_alarm', ['audio_alarm_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_carpet_trims_mats_id_fkey', 'tb_carpet_trim_mats', ['carpet_trims_mats_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_interior_heat_ac_defog_defrost_id_fkey', 'tb_heat_ac_defog_defrost', ['heat_ac_defog_defrost_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('tb_exterior', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('tb_exterior_body_panels_bumper_id_fkey', 'tb_body_bumper', ['body_panels_bumper_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_exterior_exterior_lights_id_fkey', 'tb_exterior_lights', ['exterior_lights_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_exterior_glass_outside_mirrors_id_fkey', 'tb_glass_outside_mirrors', ['glass_outside_mirrors_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_exterior_grille_trim_roof_rack_id_fkey', 'tb_grille_trim_roof_rack', ['grille_trim_roof_rack_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('tb_exterior_doors_hood_tailgate_id_fkey', 'tb_doors_hood_tailgate', ['doors_hood_tailgate_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###